import unittest
from mbpp_451_code import remove_whitespaces

class TestRemoveWhitespaces(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(remove_whitespaces("Hello World"), "HelloWorld")

    def test_empty_input(self):
        self.assertEqual(remove_whitespaces(""), "")

    def test_whitespace_only_input(self):
        self.assertEqual(remove_whitespaces("   "), "")

    def test_whitespace_with_special_characters(self):
        self.assertEqual(remove_whitespaces("Hello,   World!"), "Hello,World!")

    def test_whitespace_with_numbers(self):
        self.assertEqual(remove_whitespaces("1 2 3 4 5"), "12345")

    def test_whitespace_with_mixed_characters(self):
        self.assertEqual(remove_whitespaces("a b c d e"), "abcde")
