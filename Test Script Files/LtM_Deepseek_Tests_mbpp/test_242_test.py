import unittest
from mbpp_242_code import count_charac

class TestCountCharac(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(count_charac("hello"), 5)

    def test_empty_input(self):
        self.assertEqual(count_charac(""), 0)

    def test_single_character_input(self):
        self.assertEqual(count_charac("a"), 1)

    def test_numeric_input(self):
        self.assertEqual(count_charac("12345"), 5)

    def test_special_characters_input(self):
        self.assertEqual(count_charac("!@#$%"), 5)

    def test_whitespace_input(self):
        self.assertEqual(count_charac(" "), 1)
