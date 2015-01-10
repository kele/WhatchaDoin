__author__ = 'kele'

from PySide import QtGui, QtCore, QtUiTools
from app.ui.pyside.ContactsInfoModel import ContactsInfoModel


class PySideUI:
    def __init__(self, whatcha_doin):
        self.whatcha_doin = whatcha_doin
        self.app = QtGui.QApplication([])

        # TODO: remove hardcode
        self.main_window = self.loadUIFile('untitled.ui')

        self.tray_icon = createTrayIcon(self.main_window)

        # TODO: map objects from UI
        add_button = self.main_window.findChild(QtGui.QPushButton,
                                                'addContactButton')
        add_button.clicked.connect(self._addButtonAction)

        list_view = self.main_window.findChild(QtGui.QListView, 'contactList')
        self.contacts_model = ContactsInfoModel(self.whatcha_doin.address_book, self.whatcha_doin)
        list_view.setModel(self.contacts_model)

        busy_button = self.main_window.findChild(QtGui.QRadioButton,
                                                 'busyRadioButton')
        busy_button.clicked.connect(
            lambda: self.whatcha_doin.setBuddyStatus('busy'))

        free_button = self.main_window.findChild(QtGui.QRadioButton,
                                                 'freeRadioButton')
        free_button.clicked.connect(
            lambda: self.whatcha_doin.setBuddyStatus('free'))

        refresh_button = self.main_window.findChild(QtGui.QPushButton,
                                                    'refreshButton')
        refresh_button.clicked.connect(self.refresh)

        self.main_window.show()

    def refresh(self):
        self.whatcha_doin.refresh()

    @staticmethod
    def loadUIFile(filename):
        loader = QtUiTools.QUiLoader()
        file = QtCore.QFile(filename)
        file.open(QtCore.QFile.ReadOnly)
        main_window = loader.load(file)
        file.close()

        return main_window

    def run(self):
        retval = self.app.exec_()
        self.whatcha_doin.is_running = False
        return retval

    def _addButtonAction(self):
        name, ok = QtGui.QInputDialog.getText(self.main_window,
                                              'Name', 'Enter name:')
        if not ok:
            return

        ipaddr, ok = QtGui.QInputDialog.getText(self.main_window,
                                                'IP', 'IP:')
        if not ok:
            return

        port, ok = QtGui.QInputDialog.getText(self.main_window,
                                              'Port', 'Port:',
                                              mode=QtGui.QInputDialog.IntInput)
        port = int(port)
        if not ok:
            return

        self.contacts_model.insertItem(name, (ipaddr, port))


def createTrayIcon(main_window):
    tray_icon_menu = QtGui.QMenu(main_window)
    tray_icon_menu.addAction(QtGui.QAction("Mi&nimize", main_window,
                                           triggered=main_window.hide))
    tray_icon_menu.addAction(QtGui.QAction("&Restore", main_window,
                                           triggered=main_window.showNormal))

    tray_icon_menu.addAction(QtGui.QAction("&Quit", main_window,
                                           triggered=main_window.close))

    tray_icon = QtGui.QSystemTrayIcon(QtGui.QIcon('icons.svg'), main_window)
    tray_icon.setContextMenu(tray_icon_menu)
    tray_icon.show()

    return tray_icon


def centerWindow(window):
    desktop_geometry_center = QtGui.QDesktopWidget().screenGeometry().center()
    frame_geometry = window.frameGeometry()
    frame_geometry.moveCenter(desktop_geometry_center)
    window.move(frame_geometry.topLeft())


def createMainWindow():
    window = QtGui.QMainWindow()
    window.resize(500, 300)
    centerWindow(window)

    return window
