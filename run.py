__author__ = 'kele'

import click
import threading

from app.core.WhatchaDoin import WhatchaDoin
from app.networking.udp import UdpNetworking
from app.core.AddressBook import AddressBook
from app.ui.console import ConsoleUI


@click.command()
@click.option('--port', default = 8101, help = 'Port number')
@click.option('--name', default = 'user', help = 'Username')
def main(port, name):
    networking = UdpNetworking(port)
    whatcha_doin = WhatchaDoin(name, networking, AddressBook())
    ui = ConsoleUI(whatcha_doin)

    networkingThread = threading.Thread(target = lambda: networking.run(whatcha_doin))
    networkingThread.start()

    ui.run()


if __name__ == "__main__":
    main()








