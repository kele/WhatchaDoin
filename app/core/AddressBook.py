__author__ = 'kele'


class AddressBook:
    def __init__(self):
        self._contacts = {}

    def addContact(self, name, address):
        if name in self._contacts:
            raise Warning('Contact with this name already exists')

        if address in self._contacts.values():
            raise Warning('Contact with this address already exists')

        self._contacts[name] = address

    def deleteContact(self, name):
        del self._contacts[name]

    def findContact(self, name):
        if name in self._contacts:
            return self._contacts[name]
        else:
            return None

    def size(self):
        return len(self._contacts)

    def __iter__(self):
        return self._contacts.__iter__()
