__author__ = 'kele'

from . import AddressBook


class WhatchaDoin:
    def __init__(self, username, networking, address_book):
        self._statuses = {}
        self.address_book = address_book
        self.user_id = self.address_book.addContact(username, networking.local_address)
        self.setUserStatus('free')
        self._get_status_func = lambda addr: networking.getStatus(addr)

    def setUserStatus(self, busy_flag, desc=''):
        self.setStatus(self.user_id, busy_flag, desc)

    def setStatus(self, id, busy_flag, desc=''):
        self._statuses[id] = { 'busy_flag': busy_flag, 'desc': desc }

    def getUserStatus(self):
        return self._statuses[self.user_id]

    def getStatus(self, id):
        addr = self.address_book.contacts[id]
        return self._get_status_func(addr)




