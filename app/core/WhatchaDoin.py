__author__ = 'kele'

from . import AddressBook
from threading import Lock


class WhatchaDoin:
    def __init__(self, username, networking, address_book):
        self.address_book = address_book
        self.user_id = self.address_book.addContact(username, networking.local_address)
        self.setUserStatus('free')
        self._running = True
        self._running_lock = Lock()

        self._get_status_func = networking.getStatus

    def setUserStatus(self, busy_flag, desc=''):
        self._user_status = { 'busy_flag': busy_flag, 'desc': desc }

    def getUserStatus(self):
        return self._user_status

    def getStatus(self, id):
        addr = self.address_book.contacts[id]
        return self._get_status_func(addr)


    @property
    def is_running(self):
        with self._running_lock:
            val = self._running
        return val

    @is_running.setter
    def is_running(self, running):
        with self._running_lock:
            self._running = running





