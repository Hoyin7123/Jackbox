import socket


def main():
    print("Starting!")
    ip = input("Please input the IP address of the server: ")
    port = input("Please input the port to which you would like to connect: ")
    sock = socket.create_connection((ip, int(port)))
    print(f"Successfully connected to {ip} at port {port}.")


if __name__ == "__main__":
    main()
