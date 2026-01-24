import unittest
from mbpp_565_code import split

class TestSplit(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(split(''), [])

    def test_single_character_string(self):
        self.assertEqual(split('a'), ['a'])

    def test_multi_character_string(self):
        self.assertEqual(split('abc'), ['a', 'b', 'c'])

    def test_whitespace_string(self):
        self.assertEqual(split('   '), [' ', '\n', ' ', '\t'])

    def test_string_with_special_characters(self):
        self.assertEqual(split('!@#$%^&*()_+-=[]{}|;:,.<>?'), ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '[', ']', '{', '}', '|', ';', ':', ',', '.', '>', ' '])
