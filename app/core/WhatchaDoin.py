__author__ = 'kele'

from threading import Lock


class WhatchaDoin:
    def __init__(self, networking, address_book):
        self.address_book = address_book

        self.user_status = {'busy': 'free', 'desc': ''}

        self._running = True
        self._running_lock = Lock()

        self._buddy_statuses = {}
        self._get_status_func = networking.getStatus

    def buddyCount(self):
        return self.address_book.size()

    def setBuddyStatus(self, name, busy, desc=''):
        self._buddy_statuses[name] = {'busy':busy, 'desc':desc}


    def refresh(self):
        self._buddy_statuses.clear()

        for (name, _) in self.address_book:
            self.getFreshBuddyStatus(name)

    def getBuddyStatus(self, name):
        if name in self._buddy_statuses:
            return self._buddy_statuses[name]
        else:
            return self.getFreshBuddyStatus(name)

    def getFreshBuddyStatus(self, name):
        addr = self.address_book.contacts[name]
        status = self._get_status_func(addr)
        self._buddy_statuses[name] = status
        return status

    @property
    def is_running(self):
        with self._running_lock:
            val = self._running
        return val

    @is_running.setter
    def is_running(self, running):
        with self._running_lock:
            self._running = running
