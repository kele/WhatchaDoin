__author__ = 'kele'

import threading

import click

from src.core.WhatchaDoin import WhatchaDoin
from src.ui.console import ConsoleUI
from src.networking.udp import UdpNetworking


@click.command()
@click.option('--port', default = 8101, help = 'Port number')
@click.option('--name', default = 'user', help = 'Username')
def main(port, name):
    networking = UdpNetworking(port)
    whatcha_doin = WhatchaDoin(name, networking)

    ui = ConsoleUI(whatcha_doin)

    networkingThread = threading.Thread(target = lambda: networking.run(whatcha_doin))
    uiThread = threading.Thread(target = ui.run)

    networkingThread.start()
    uiThread.start()

if __name__ == "__main__":
    main()








