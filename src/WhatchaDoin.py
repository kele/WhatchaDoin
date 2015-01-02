__author__ = 'kele'

from src.AddressBook import AddressBook

class WhatchaDoin:
    def __init__(self, username, networking):
        self.statuses = {}
        self.address_book = AddressBook()
        self.user_id = self.address_book.addContact(username, networking.local_address)
        self.setUserStatus('free')
        self.get_status_func = lambda addr: networking.getStatus(addr)

    def setUserStatus(self, busy_flag, desc=''):
        self.setStatus(self.user_id, busy_flag, desc)

    def setStatus(self, id, busy_flag, desc=''):
        self.statuses[id] = { 'busy_flag': busy_flag, 'desc': desc }

    def getUserStatus(self):
        return self.statuses[self.user_id]

    def getStatus(self, id):
        addr = self.address_book.contacts[id]
        return self.get_status_func(addr)




