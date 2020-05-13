import socketserver

from server.TCPHandler import TCPHandler

global send, msg
send = []
msg = []


def main():
    print("Starting!")
    port = input("Please input a port number: ")
    ip = "localhost"  # TODO: Figure out how to get public IP
    with socketserver.TCPServer((ip, int(port)), TCPHandler) as server:
        print(f"Started server at {ip} with port {port}.")
        server.serve_forever()


if __name__ == "__main__":
    main()
