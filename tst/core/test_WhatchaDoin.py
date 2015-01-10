__author__ = 'kele'

import unittest
from unittest.mock import MagicMock

from app.core.WhatchaDoin import WhatchaDoin


USERNAME = 'FakeUsername'
DEFAULT_FREE_STATUS = {'busy': 'free', 'desc': ''}
BUSY_STATUS_1 = {'busy': 'busy', 'desc': 'working'}
BUSY_STATUS_2 = {'busy': 'busy', 'desc': 'mailing'}
FAKE_ADDRESS = {'192.168.0.1', 8101}


class TestWhatchaDoin(unittest.TestCase):
    def setUp(self):
        self.networking = MagicMock()
        self.address_book = MagicMock()

    def test_init(self):
        sut = WhatchaDoin(self.networking, self.address_book)

        self.assertEqual(sut.user_status, DEFAULT_FREE_STATUS)

    def test_getBuddyStatus(self):
        self.networking.getStatus = MagicMock(return_value=BUSY_STATUS_2)

        sut = WhatchaDoin(self.networking, self.address_book)

        self.address_book.contacts = MagicMock()
        self.address_book.contacts.__getitem__.return_value = FAKE_ADDRESS

        returned_status = sut.getBuddyStatus('fakename')

        self.assertEqual(returned_status, BUSY_STATUS_2)
        self.networking.getStatus.assert_called_with(FAKE_ADDRESS)

    def test_getBuddyStatus_dontUseNetworkingWhenAlreadyCached(self):
        self.networking.getStatus = MagicMock(return_value=BUSY_STATUS_2)

        sut = WhatchaDoin(self.networking, self.address_book)

        self.address_book.contacts = MagicMock()
        self.address_book.contacts.__getitem__.return_value = FAKE_ADDRESS

        returned_status = sut.getBuddyStatus('fakename')

        self.assertEqual(returned_status, BUSY_STATUS_2)
        self.networking.getStatus.assert_called_with(FAKE_ADDRESS)

        # Second time
        self.networking.getStatus = MagicMock()

        returned_status = sut.getBuddyStatus('fakename')
        self.assertEqual(returned_status, BUSY_STATUS_2)

        assert not self.networking.getStatus.called

    def test_refresh(self):
        # TODO
        pass
