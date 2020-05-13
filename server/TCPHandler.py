import socketserver
import threading


def loopback():
    while True:
        pass


class TCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        threading.Thread(target=loopback).start()
