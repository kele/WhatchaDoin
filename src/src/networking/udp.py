__author__ = 'kele'

from socketserver import UDPServer, BaseRequestHandler
import socket
import logging

class RequestHandler(BaseRequestHandler):
    def __init__(self, whatcha_doin, *args):
        self.whatcha_doin = whatcha_doin
        super().__init__(*args)

    def handle(self):
        data = str(self.request[0].strip(), 'utf-8')
        socket = self.request[1]

        if data == 'getstatus':
            my_status = self.whatcha_doin.getUserStatus()
            msg = bytes(str(my_status), 'utf-8')
            socket.sendto(msg, self.client_address)
        else:
            logging.error(data)
            msg = bytes(str('Unknown command'), 'utf-8')
            socket.sendto(msg, self.client_address)

class Server:
    def run(self, whatcha_doin, port):
        server = UDPServer(("localhost", port), lambda *args: RequestHandler(whatcha_doin, *args))
        server.serve_forever()


class UdpNetworking:
    def __init__(self, port):
        self.server = Server()
        self.port = port
        self.local_address = ('localhost', self.port)

    def run(self, whatcha_doin):
        self.server.run(whatcha_doin, self.port)

    def getStatus(self, address):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        msg = bytes('getstatus', 'utf-8')
        sock.sendto(msg, address)
        received = str(sock.recv(1024), 'utf-8')
        return received


