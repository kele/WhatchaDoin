__author__ = 'kele'


import unittest
from unittest.mock import MagicMock

from app.ui.pyside.BuddyInfoModel import BuddyInfoModel

class TestBuddyInfoModel(unittest.TestCase):
    def setUp(self):
        self.buddy_info = MagicMock()
        pass

    def test_rowCount(self):
        self.buddy_info.buddyCount = MagicMock(return_value=3)

        sut = BuddyInfoModel(self.buddy_info)
        self.assertEqual(sut.rowCount(), 3)
        assert self.buddy_info.buddyCount.call_count == 1

    def test_init(self):
        # check if patches are made

        self.buddy_info.setBuddyStatus = MagicMock()
        old_buddy_status_method = self.buddy_info.setBuddyStatus

        sut = BuddyInfoModel(self.buddy_info)

        self.buddy_info.setBuddyStatus('buddy', 'busy', 'description')
        old_buddy_status_method.assert_called_once_with('buddy', 'busy', 'description')