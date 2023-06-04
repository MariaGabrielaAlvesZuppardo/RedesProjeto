import socket

def run_client_publisher(topic):
    publisher_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    publisher_socket.connect(('127.0.0.1', 5555))
    print("Conectando ao servidor de publicação...")

    while True:
        message = input("Digite a mensagem que você irá publicar: ")
        full_message = f"{topic}:{message}"
        publisher_socket.send(full_message.encode())
        print("Mensagem publicada com sucesso")

    publisher_socket.close()

if __name__ == "__main__":
    topic = input("Digite o tópico que você deseja publicar: ")
    run_client_publisher(topic)

