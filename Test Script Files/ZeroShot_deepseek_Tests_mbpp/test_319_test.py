import unittest
from mbpp_319_code import find_long_word

class TestFindLongWord(unittest.TestCase):

    def test_find_long_word(self):
        self.assertEqual(find_long_word("Hello world"), [])
        self.assertEqual(find_long_word("This is a test string"), ['string'])
        self.assertEqual(find_long_word("This is a test string with long words"), ['string', 'long', 'words'])
        self.assertEqual(find_long_word(""), [])
        self.assertEqual(find_long_word("a"), [])
        self.assertEqual(find_long_word("abcdefghijklmnopqrstuvwxyz"), ['abcdefghijklmnopqrstuvwxyz'])
        self.assertEqual(find_long_word("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"), ['abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'])
        self.assertEqual(find_long_word("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"), [])
