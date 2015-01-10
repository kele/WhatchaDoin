__author__ = 'kele'

from PySide.QtCore import QAbstractListModel

class BuddyInfoModel(QAbstractListModel):
    def __init__(self, buddy_info):
        self._buddy_info = buddy_info

        def patchedSetBuddyStatus(obj, *args, **kwargs):
            obj.setBuddyStatus(*args, **kwargs)
            self.dataChanged.emit(self.index(0, 0), self.index(self.rowCount() - 1, 0))

        self._old_setBuddyStatus = self._buddy_info.setBuddyStatus
        self._buddy_info.setBuddyStatus = patchedSetBuddyStatus

    def __del__(self):
        pass

    def rowCount(self):
        return self._buddy_info.buddyCount()
