import unittest
from mbpp_565_code import split

class TestSplitFunction(unittest.TestCase):

    def test_single_character(self):
        self.assertEqual(split('a'), ['a'])

    def test_multiple_characters(self):
        self.assertEqual(split('abc'), ['a', 'b', 'c'])

    def test_empty_string(self):
        self.assertEqual(split(''), [])

    def test_numeric_string(self):
        self.assertEqual(split('123'), ['1', '2', '3'])

    def test_string_with_spaces(self):
        self.assertEqual(split('hello world'), ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd'])
