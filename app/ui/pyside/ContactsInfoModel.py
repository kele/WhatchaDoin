__author__ = 'kele'

from PySide import QtCore

# TODO: rewrite this


# TODO: refactoring
# TODO: UT
class ContactsInfoModel(QtCore.QAbstractListModel):
    def __init__(self, address_book, whatcha_doin):
        super().__init__()

        self.address_book = address_book
        self._patchAddressBook()

        self.whatcha_doin = whatcha_doin

    def rowCount(self, *args, **kwargs):
        return self.address_book.size()

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            if index.row() < self.address_book.size():
                sorted_items = sorted(list(self.address_book.contacts.items()), key=lambda e: e[0].lower())
                user_info = sorted_items[index.row()]
                username = user_info[0]
                ip = user_info[1][0]
                port = str(user_info[1][1])
                raw_status = self.whatcha_doin.getBuddyStatus(username)
                status = raw_status['busy'] + '(' + raw_status['desc'] + ')'
                return username + '[' + ip + ':' + port + "] -- " + status
            else:
                return None
        else:
            return None

    def insertItem(self, name, addr):
        self.address_book.addContact(name, addr)
        self.dataChanged.emit(self.index(0, 0), self.index(self.rowCount() - 1, 0))

    def _unpatchAddressBook(self):
        pass


    def __del__(self):
        self.unpatchAddressBook()

    def _patchAddressBook(self):
        def patchedAddContact(obj, name, addr):
            obj.addContact(name, addr)
            self.dataChanged.emit(self.index(0, 0), self.index(self.rowCount() - 1, 0))

        self.address_book.addContact = patchedAddContact
