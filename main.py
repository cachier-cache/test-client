import socket


def client_program():
    host = "localhost"
    port = 8080

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input(" -> ")

    while message.lower().strip() != "exit":
        # client_socket.send(message.encode())
        # client_socket.send(message.encode())
        # client_socket.send(message.encode())
        # client_socket.send(message.encode())

        # added \n to the end for the server to recognize
        # the end of the message
        client_socket.send((message + "\n").encode())
        data = client_socket.recv(1024).decode()
        print(f'Received from server: {data}')

        message = input(" -> ")

    client_socket.close()


if __name__ == "__main__":
    client_program()
