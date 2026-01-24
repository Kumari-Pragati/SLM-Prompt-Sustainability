import unittest
from mbpp_565_code import split

class TestSplitFunction(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(split("hello"), ["h", "e", "l", "l", "o"])

    def test_single_character_input(self):
        self.assertEqual(split("a"), ["a"])

    def test_empty_input(self):
        self.assertEqual(split(""), [])

    def test_whitespace_input(self):
        self.assertEqual(split("   "), [" ", "\t"])

    def test_special_characters_input(self):
        self.assertEqual(split("!@#$%^&*()_+-=[]{}|;:'\",.<>?/"),
                         ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
                          "+", "-", "=", "[", "]", "{", "}", "|", ";", ":",
                          "'", '"', "<", ">", ">", "/"])
