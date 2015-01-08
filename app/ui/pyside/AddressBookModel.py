__author__ = 'kele'

from PySide import QtCore

# TODO: refactoring
# TODO: UT
class AddressBookModel(QtCore.QAbstractListModel):
    def __init__(self, address_book):
        super().__init__()
        self.address_book = address_book

    def rowCount(self, *args, **kwargs):
        return self.address_book.size()

    def data(self, index, role = QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            if index.row() < self.address_book.size():
                sorted_items = sorted(list(self.address_book.contacts.items()), key=lambda e: e[0].lower())
                user = sorted_items[index.row()]
                return user[0] + ' ' + user[1][0] + ':' + str(user[1][1])
            else:
                return None
        else:
            return None

    def insertItem(self, name, addr):
        self.address_book.addContact(name, addr)
        self.dataChanged.emit(self.index(0, 0), self.index(self.rowCount() - 1, 0))


