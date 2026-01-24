import unittest
from mbpp_565_code import split

class TestSplit(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(split(""), [])

    def test_single_character(self):
        self.assertEqual(split("a"), ['a'])

    def test_multiple_characters(self):
        self.assertEqual(split("hello"), ['h', 'e', 'l', 'l', 'o'])

    def test_spaces(self):
        self.assertEqual(split("hello world"), ['h', 'e', 'l', 'l', 'o','', 'w', 'o', 'r', 'l', 'd'])

    def test_punctuation(self):
        self.assertEqual(split("hello, world!"), ['h', 'e', 'l', 'l', 'o', ',','', 'w', 'o', 'r', 'l', 'd', '!'])

    def test_newline(self):
        self.assertEqual(split("hello\nworld"), ['h', 'e', 'l', 'l', 'o', '\n', 'w', 'o', 'r', 'l', 'd'])

    def test_tabs(self):
        self.assertEqual(split("hello\tworld"), ['h', 'e', 'l', 'l', 'o', '\t', 'w', 'o', 'r', 'l', 'd'])

    def test_mixed_characters(self):
        self.assertEqual(split("hello123!"), ['h', 'e', 'l', 'l', 'o', '1', '2', '3', '!'])

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            split(123)
