import unittest
from mbpp_7_code import find_char_long

class TestFindCharLong(unittest.TestCase):

    def test_find_char_long(self):
        self.assertEqual(find_char_long("Hello world"), ['Hello', 'world'])
        self.assertEqual(find_char_long("Python is awesome"), ['Python', 'awesome'])
        self.assertEqual(find_char_long("This is a test"), ['This', 'test'])
        self.assertEqual(find_char_long(""), [])
        self.assertEqual(find_char_long("a"), [])
        self.assertEqual(find_char_long("1234567890"), [])
        self.assertEqual(find_char_long("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"), ['abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'])
