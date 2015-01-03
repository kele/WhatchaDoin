__author__ = 'kele'

class AddressBook:
    def __init__(self):
        self.contacts = {}
        self.last_contact = 0

    def addContact(self, name, address):
        id = self.last_contact
        self.contacts[id] = address

        self.last_contact += 1
        return id

    def deleteContact(self, id):
        raise NotImplementedError

    def findContact(self, query):
        raise NotImplementedError

    def listContacts(self):
        return str(self.contacts)
