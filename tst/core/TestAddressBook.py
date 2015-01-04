__author__ = 'kele'

import unittest

from app.core.AddressBook import AddressBook

ADDRESS_1 = ('111.111.111.111', 1337)
ADDRESS_2 = ('111.111.111.111', 1338)
class TestAddressBook(unittest.TestCase):
    def setUp(self):
        self.sut = AddressBook()

    def test_init(self):
        self.assertEqual(self.sut.contacts, {})

    def test_addContact_new(self):
        id_1 = self.sut.addContact('fakename', ADDRESS_1)

        self.assertEqual(self.sut.contacts[id_1], ADDRESS_1)
        self.assertEqual(self.sut.size(), 1)

        id_2 = self.sut.addContact('fakename2', ADDRESS_2)

        self.assertEqual(self.sut.contacts[id_2], ADDRESS_2)
        self.assertEqual(self.sut.size(), 2)

    def test_addContact_existingName(self):
        self.sut.addContact('fakename', ADDRESS_1)
        self.assertRaises(Warning, self.sut.addContact, 'fakename', ADDRESS_2)

        self.assertEqual(self.sut.size(), 1)

    def test_addContact_existingAddress(self):
        self.sut.addContact('fakename', ADDRESS_1)
        self.assertRaises(Warning, self.sut.addContact, 'othername', ADDRESS_1)

        self.assertEqual(self.sut.size(), 1)

    def test_size(self):
        ids = []
        for i in range(0, 10):
            ids.append(self.sut.addContact('fakename' + str(i), ('111.111.111.111', 1337 + i)))

        self.assertEqual(self.sut.size(), 10)

        for i in range(0, 10):
            self.sut.deleteContact('fakename' + str(i))

        self.assertEqual(self.sut.size(), 0)


    def test_deleteContact_exists(self):
        id = self.sut.addContact('fakaname', ADDRESS_1)

        self.sut.deleteContact(id)
        self.assertEqual(self.sut.size(), 0)

    def test_deleteContact_notExists(self):
        self.assertRaises(KeyError, self.sut.deleteContact, id)

    def test_findContact_exists(self):
        self.sut.addContact('fakename', ADDRESS_1)

        self.assertEqual(self.sut.findContact('fakename'), ADDRESS_1)

    def test_findContact_notExists(self):
        self.assertEqual(self.sut.findContact('fakename'), None)

