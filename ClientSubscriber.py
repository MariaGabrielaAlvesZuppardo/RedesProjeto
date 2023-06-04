import socket

def run_client_subscriber(topic):
    subscriber_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    subscriber_socket.connect(('127.0.0.1', 5556))  
    print("Conectado ao servidor de assinatura")

    
    subscribe_command = f"SUBSCRIBE {topic}"
    subscriber_socket.send(subscribe_command.encode())
    print(f"Inscrito no tópico {topic}")

    while True:
        message = subscriber_socket.recv(1024).decode()
        if message:
            if message == "FINISH":
                break  
            print("Nova mensagem recebida:", message)

    subscriber_socket.close()

if __name__ == "__main__":
    topic = input("Digite o tópico para assinar: ")
    run_client_subscriber(topic)