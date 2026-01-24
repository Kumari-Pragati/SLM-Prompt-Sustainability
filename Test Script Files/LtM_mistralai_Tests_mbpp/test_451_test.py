import unittest
from mbpp_451_code import remove_whitespaces

class TestRemoveWhitespaces(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(remove_whitespaces("Hello World"), "HelloWorld")

    def test_single_space(self):
        self.assertEqual(remove_whitespaces(" "), "")

    def test_multiple_spaces(self):
        self.assertEqual(remove_whitespaces("   Hello World   "), "HelloWorld")

    def test_leading_trailing_spaces(self):
        self.assertEqual(remove_whitespaces(" Hello World "), "HelloWorld")

    def test_empty_string(self):
        self.assertEqual(remove_whitespaces(""), "")

    def test_newline(self):
        self.assertEqual(remove_whitespaces("\nHello World\n"), "HelloWorld")

    def test_tab(self):
        self.assertEqual(remove_whitespaces("\tHello World\t"), "HelloWorld")
