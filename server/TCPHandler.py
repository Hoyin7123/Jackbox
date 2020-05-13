import socketserver
import threading

from server.Server import send, msg


class TCPHandler(socketserver.BaseRequestHandler):
    def loopback(self):
        while True:
            if not send == []:
                for s in send:
                    for strings in msg:
                        pass

    def handle(self):
        send.append(self)
        threading.Thread(target=self.loopback).start()
