__author__ = 'kele'

import click
import threading

from app.core.WhatchaDoin import WhatchaDoin
from app.networking.udp import UdpNetworking
from app.core.AddressBook import AddressBook

from app.ui.pyside.pyside import PySideUI


@click.command()
@click.option('--port', default=8104, help='Port number')
def main(port):
    networking = UdpNetworking(port)
    whatcha_doin = WhatchaDoin(networking, AddressBook())
    ui = PySideUI(whatcha_doin)

    networkingThread =\
        threading.Thread(target=lambda: networking.run(whatcha_doin))

    networkingThread.start()

    ui.run()
    networkingThread.join()


if __name__ == "__main__":
    main()
