__author__ = 'kele'

class AddressBook:
    def __init__(self):
        self.contacts = {}

    def addContact(self, name, address):
        if name in self.contacts:
            raise Warning('Contact with this name already exists')

        if address in self.contacts.values():
            raise Warning('Contact with this address already exists')

        self.contacts[name] = address
        return name

    def deleteContact(self, id):
        del self.contacts[id]

    def findContact(self, query):
        if query in self.contacts:
            return self.contacts[query]
        else:
            return None

    def size(self):
        return len(self.contacts)
