import unittest
from mbpp_15_code import split_lowerstring

class TestSplitLowerString(unittest.TestCase):

    def test_split_lowerstring(self):
        self.assertEqual(split_lowerstring("HelloWorld"), ["hello", "world"])
        self.assertEqual(split_lowerstring("Hello123World"), ["hello", "123", "world"])
        self.assertEqual(split_lowerstring("HelloWorld123"), ["hello", "world", "123"])
        self.assertEqual(split_lowerstring("Hello123World456"), ["hello", "123", "world", "456"])
        self.assertEqual(split_lowerstring("HelloWorld123World456"), ["hello", "world", "123", "world", "456"])
        self.assertEqual(split_lowerstring("HelloWorld123World456789"), ["hello", "world", "123", "world", "456", "789"])
        self.assertEqual(split_lowerstring("HelloWorld123World4567890"), ["hello", "world", "123", "world", "456", "789", "0"])
        self.assertEqual(split_lowerstring("HelloWorld123World4567890abc"), ["hello", "world", "123", "world", "456", "789", "0", "abc"])
        self.assertEqual(split_lowerstring("HelloWorld123World4567890abcdef"), ["hello", "world", "123", "world", "456", "789", "0", "abc", "def"])
        self.assertEqual(split_lowerstring("HelloWorld123World4567890abcdefg"), ["hello", "world", "123", "world", "456", "789", "0", "abc", "def", "g"])
        self.assertEqual(split_lowerstring("HelloWorld123World4567890abcdefg123"), ["hello", "world", "123", "world", "456", "789", "0", "abc", "def", "g", "123"])
        self.assertEqual(split_lowerstring("HelloWorld123World4567890abcdefg123456"), ["hello", "world", "123", "world", "456", "789", "0", "abc", "def", "g", "123", "456"])
        self.assertEqual(split_lowerstring("HelloWorld123World4567890abcdefg123456789"), ["hello", "world", "123", "world", "456", "789", "0", "abc", "def", "g", "123", "456", "789"])
        self.assertEqual(split_lowerstring("HelloWorld123World4567890abcdefg1234567890"), ["hello", "world", "123", "world", "456", "789", "0", "abc", "def", "g", "123", "456", "789", "0"])
        self.assertEqual(split_lowerstring("HelloWorld123World4567890abcdefg1234567890abc"), ["hello", "world", "123", "world", "456", "789", "0", "abc", "def", "g", "123", "456", "789", "0", "abc"])
        self.assertEqual(split_lowerstring("HelloWorld123World4567890abcdefg1234567890abcdef"), ["hello", "world", "123", "world", "456", "789", "0", "abc", "def", "g", "123", "456", "789", "0", "abc", "def"])
        self.assertEqual(split_lowerstring("HelloWorld123World4567890abcdefg1234567890abcdefg"), ["hello", "world", "123", "world", "456", "789", "0", "abc", "def", "g", "123", "456", "789", "0", "abc", "def", "g"])
        self.assertEqual(split_lowerstring("HelloWorld123World4567890abcdefg1234567890abcdefg123"), ["hello", "world", "123", "world", "456", "789", "0", "abc", "def", "g", "123", "456", "789", "0", "abc", "def", "g", "123"])
        self.assertEqual(split_lowerstring("HelloWorld123World4567890abcdefg1234567890abcdefg123456"), ["hello", "world", "123", "world", "456", "789", "0", "abc", "def", "g", "123", "456", "789", "0", "abc", "def", "g", "123", "456"])
        self.assertEqual(split_lowerstring("HelloWorld123World4567890abcdefg1234567890abcdefg123456789"), ["hello", "world", "123", "world", "456", "789", "0", "abc", "def", "g", "123", "456", "789", "0", "abc", "def", "g", "123", "456", "789"])
        self.assertEqual