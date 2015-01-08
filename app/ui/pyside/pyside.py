__author__ = 'kele'

import sys
from PySide import QtGui, QtCore, QtUiTools

from app.ui.pyside.AddressBookModel import AddressBookModel

class PySideUI:
    def __init__(self, whatcha_doin):
        self.whatcha_doin = whatcha_doin
        self.app = QtGui.QApplication([])

        # TODO: remove hardcode
        self.loadUIFile('untitled.ui')

        # TODO: map objects from UI
        add_button = self.main_window.findChild(QtGui.QPushButton, 'addContactButton')
        assert isinstance(add_button, QtGui.QPushButton)
        add_button.clicked.connect(self._addButtonAction)

        self.list_view = self.main_window.findChild(QtGui.QListView, 'contactList')
        self.contacts_model = AddressBookModel(self.whatcha_doin.address_book)
        self.list_view.setModel(self.contacts_model)

        self.main_window.show()

    def loadUIFile(self, filename):
        loader = QtUiTools.QUiLoader()
        file = QtCore.QFile(filename)
        file.open(QtCore.QFile.ReadOnly)
        self.main_window = loader.load(file)
        file.close()

    def run(self):
        sys.exit(self.app.exec_())

    def _addButtonAction(self):
        name, ok = QtGui.QInputDialog.getText(self.main_window, 'Name', 'Enter name:')
        if not ok: return

        ipaddr, ok = QtGui.QInputDialog.getText(self.main_window, 'IP', 'IP:')
        if not ok: return

        port, ok = QtGui.QInputDialog.getText(self.main_window, 'Port', 'Port:', mode = QtGui.QInputDialog.IntInput)
        port = int(port)
        if not ok: return

        self.contacts_model.insertItem(name, (ipaddr, port))


def centerWindow(window):
    desktop_geometry_center = QtGui.QDesktopWidget().screenGeometry().center()
    frame_geometry = window.frameGeometry()
    frame_geometry.moveCenter(desktop_geometry_center)
    window.move(frame_geometry.topLeft())

def createMainWindow(whatcha_doin):
    window = QtGui.QMainWindow()
    window.resize(500, 300)
    centerWindow(window)

    return window

