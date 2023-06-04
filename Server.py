import socket
import threading

class SubscriberThread(threading.Thread):
    def __init__(self, client_socket):
        threading.Thread.__init__(self)
        self.client_socket = client_socket

    def run(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                if message:
                    print("Nova mensagem recebida:", message)
            except:
                break

class Server:
    def __init__(self):
        self.subscriber_threads = []
        self.topic_subscribers = {}
        self.topic_last_message = {}
        self.lock = threading.Lock()  # Adicionado um objeto Lock

    def run(self):
        subscriber_server_thread = threading.Thread(target=self.start_subscriber_server)
        publisher_server_thread = threading.Thread(target=self.start_publisher_server)

        subscriber_server_thread.start()
        publisher_server_thread.start()

        subscriber_server_thread.join()
        publisher_server_thread.join()

    def start_publisher_server(self):
        publisher_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        publisher_server_socket.bind(('127.0.0.1', 5555))
        publisher_server_socket.listen(5)

        while True:
            client_socket, address = publisher_server_socket.accept()
            print("Novo publicador conectado:", address)
            threading.Thread(target=self.handle_publisher, args=(client_socket,)).start()

    def handle_publisher(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if message:
                    topic, data = message.split(':', 1)
                    with self.lock:  # Bloqueio para acessar os dados compartilhados
                        if topic in self.topic_subscribers:
                            subscribers = self.topic_subscribers[topic]
                            self.topic_last_message[topic] = data
                            for subscriber in subscribers:
                                subscriber.send(data.encode())
            except:
                client_socket.close()
                break

    def start_subscriber_server(self):
        subscriber_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        subscriber_server_socket.bind(('127.0.0.1', 5556))  # Alterando a porta para evitar conflito com o servidor de publicadores
        subscriber_server_socket.listen(5)

        while True:
            client_socket, address = subscriber_server_socket.accept()
            print("Novo assinante conectado:", address)
            threading.Thread(target=self.handle_subscriber, args=(client_socket,)).start()

    def handle_subscriber(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if message:
                    if message.startswith("SUBSCRIBE"):
                        topic = message.split()[1]
                        with self.lock:  # Bloqueio para acessar os dados compartilhados
                            if topic not in self.topic_subscribers:
                                self.topic_subscribers[topic] = []
                            self.topic_subscribers[topic].append(client_socket)
                            print(f"Assinante conectado ao tópico {topic}")
                            if topic in self.topic_last_message:
                                last_message = self.topic_last_message[topic]
                                client_socket.send(last_message.encode())
                    elif message.startswith("UNSUBSCRIBE"):
                        topic = message.split()[1]
                        with self.lock:  # Bloqueio para acessar os dados compartilhados
                            if topic in self.topic_subscribers:
                                self.topic_subscribers[topic].remove(client_socket)
                                if len(self.topic_subscribers[topic]) == 0:
                                    del self.topic_subscribers[topic]
                                    del self.topic_last_message[topic]
                                    print(f"Todos os assinantes desconectados do tópico {topic}")
                                else:
                                    print(f"Assinante desconectado do tópico {topic}")
            except:
                client_socket.close()
                break

if __name__ == "__main__":
    server = Server()
    server.run()
