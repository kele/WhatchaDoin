__author__ = 'kele'

import click

class ConsoleUI:
    def __init__(self, whatcha_doin):
        self.whatcha_doin = whatcha_doin
        self.user_id = self.whatcha_doin.user_id

    def run(self):
        self._greet()

        while True:
            click.echo('Current status: ' + str(self.whatcha_doin.getUserStatus()))

            input = click.prompt('[add] contact, [get] info about someone, [update] your status?').lower()

            if input == 'add':
                self._add()
            elif input == 'get':
                self._get()
            elif input == 'update':
                self._update()
            else:
                click.echo('Unknown command: ' + input)

    def _greet(self):
        click.echo("Hi!")

    def _add(self):
        name = click.prompt('Name')
        ipaddr = click.prompt('IP Address')
        port = int(click.prompt('Port'))

        self.whatcha_doin.address_book.addContact(name, (ipaddr, port))

    def _get(self):
        click.echo(self.whatcha_doin.address_book.listContacts())

        id = int(click.prompt("Id of contact to check status"))
        status = self.whatcha_doin.getStatus(id)
        click.echo("Status: " + status)

    def _update(self):
        input = click.prompt("Busy?").lower()

        if input == 'yes':
            self.whatcha_doin.setUserStatus('busy')
        elif input == 'no':
            self.whatcha_doin.setUserStatus('free')
        else:
            click.echo('Incorrect answer (yes/no)')






