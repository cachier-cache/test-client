import socket


def client_program():
    host = "localhost"
    port = 4000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input(" -> ")

    while message.lower().strip() != "exit":
        # added \n to the end for the server to recognize
        # the end of the message
        client_socket.send((message + "\n").encode())
        data = client_socket.recv(1024).decode()

        # if data is an empty string, the server has closed the connection
        if not data:
            print("Server has closed the connection.")
            break

        print(f'Received from server: {data}')

        message = input(" -> ")

    client_socket.close()


if __name__ == "__main__":
    client_program()
