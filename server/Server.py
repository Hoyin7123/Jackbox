import socketserver

from server.TCPHandler import TCPHandler


def main():
    print("Starting!")
    port = input("Please input a port number: ")
    ip = ""  # TODO: Figure out how to get public IP
    server = socketserver.TCPServer((port, ip), TCPHandler())
    print(f"Started server at ${ip} with port ${port}.")
    server.serve_forever()


if __name__ == "__main__":
    main()
