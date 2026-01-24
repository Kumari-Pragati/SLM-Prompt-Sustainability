import unittest
from mbpp_565_code import split

class TestSplitFunction(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(split(""), [])

    def test_single_character_string(self):
        self.assertEqual(split("a"), ["a"])

    def test_multi_character_string(self):
        self.assertEqual(split("abc"), ["a", "b", "c"])

    def test_string_with_spaces(self):
        self.assertEqual(split("hello world"), ["h", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d"])

    def test_string_with_special_characters(self):
        self.assertEqual(split("!@#$%^&*()_+-=[]{};:'\",.<>/?ABCDEFGHIJKLMNOPQRSTUVWXYZ"), ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "{", "[", "]", "", "}", ":", ";", ":", "'", '"', "<", ">", "/", "?", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])
