__author__ = 'kele'

import click
import sys
import threading

from app.core.WhatchaDoin import WhatchaDoin
from app.networking.udp import UdpNetworking
from app.core.AddressBook import AddressBook
from app.ui.console import ConsoleUI

from app.ui.pyside.pyside import PySideUI

@click.command()
@click.option('--port', default = 8104, help = 'Port number')
@click.option('--name', default = 'user', help = 'Username')
def main(port, name):
    networking = UdpNetworking(port)
    whatcha_doin = WhatchaDoin(name, networking, AddressBook())
    ui = PySideUI(whatcha_doin) #ConsoleUI(whatcha_doin)

    networkingThread = threading.Thread(target = lambda: networking.run(whatcha_doin))
    networkingThread.start()

    ui.run()
    networkingThread.join()


if __name__ == "__main__":
    main()








