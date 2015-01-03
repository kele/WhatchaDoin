__author__ = 'kele'

from app.core.WhatchaDoin import WhatchaDoin
import unittest
from unittest.mock import MagicMock

USERNAME = 'FakeUsername'
USER_ID = 10
DEFAULT_FREE_STATUS = { 'busy_flag':'free', 'desc':''}

class TestWhatchaDoin(unittest.TestCase):
    def setUp(self):
        self.networking = MagicMock()
        self.networking.local_address = ('127.0.0.1', 8100)
        self.address_book = MagicMock()

    def test_init(self):
        self.address_book.addContact = MagicMock(return_value = USER_ID)

        sut = WhatchaDoin(USERNAME, self.networking, self.address_book)

        self.address_book.addContact.assert_called_with(USERNAME, self.networking.local_address)
        self.assertEqual(sut.user_id, USER_ID)
        self.assertEqual(sut.getUserStatus(), DEFAULT_FREE_STATUS)


if __name__ == '__main__':
    unittest.main()

