__author__ = 'kele'

import unittest
from unittest.mock import MagicMock

from app.core.WhatchaDoin import WhatchaDoin


USERNAME = 'FakeUsername'
USER_ID = 10
FAKE_ID = 123123
DEFAULT_FREE_STATUS = { 'busy_flag':'free', 'desc':''}
BUSY_STATUS_1 = { 'busy_flag':'busy', 'desc':'working'}
BUSY_STATUS_2 = { 'busy_flag':'busy', 'desc':'mailing'}
FAKE_ADDRESS = { '192.168.0.1', 8101 }

class TestWhatchaDoin(unittest.TestCase):
    def setUp(self):
        self.networking = MagicMock()
        self.networking.local_address = ('127.0.0.1', 8100)
        self.address_book = MagicMock()
        self.address_book.addContact = MagicMock(return_value = USER_ID)

    def test_init(self):
        sut = WhatchaDoin(USERNAME, self.networking, self.address_book)

        self.address_book.addContact.assert_called_with(USERNAME, self.networking.local_address)
        self.assertEqual(sut.user_id, USER_ID)
        self.assertEqual(sut.getUserStatus(), DEFAULT_FREE_STATUS)

    def test_setUserStatus(self):
        sut = WhatchaDoin(USERNAME, self.networking, self.address_book)

        sut.setUserStatus(BUSY_STATUS_1['busy_flag'], BUSY_STATUS_1['desc'])
        self.assertEqual(sut.getUserStatus(), BUSY_STATUS_1)

        sut.setUserStatus(BUSY_STATUS_2['busy_flag'], BUSY_STATUS_2['desc'])
        self.assertEqual(sut.getUserStatus(), BUSY_STATUS_2)

        sut.setUserStatus(DEFAULT_FREE_STATUS['busy_flag'], DEFAULT_FREE_STATUS['desc'])
        self.assertEqual(sut.getUserStatus(), DEFAULT_FREE_STATUS)

    def test_getStatus(self):
        self.networking.getStatus = MagicMock(return_value = BUSY_STATUS_2)

        sut = WhatchaDoin(USERNAME, self.networking, self.address_book)

        self.address_book.contacts = MagicMock()
        self.address_book.contacts.__getitem__.return_value = FAKE_ADDRESS

        returned_status = sut.getStatus(FAKE_ID)

        self.assertEqual(returned_status, BUSY_STATUS_2)
        self.networking.getStatus.assert_called_with(FAKE_ADDRESS)
