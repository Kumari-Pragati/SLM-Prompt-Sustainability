import unittest
from mbpp_565_code import split

class TestSplitFunction(unittest.TestCase):

    def test_split_empty_string(self):
        self.assertEqual(split(""), [])

    def test_split_single_character(self):
        self.assertEqual(split("a"), ['a'])

    def test_split_multiple_characters(self):
        self.assertEqual(split("hello"), ['h', 'e', 'l', 'l', 'o'])

    def test_split_string_with_spaces(self):
        self.assertEqual(split("hello world"), ['h', 'e', 'l', 'l', 'o','', 'w', 'o', 'r', 'l', 'd'])

    def test_split_string_with_punctuation(self):
        self.assertEqual(split("Hello, world!"), ['H', 'e', 'l', 'l', 'o', ',','', 'w', 'o', 'r', 'l', 'd', '!'])
