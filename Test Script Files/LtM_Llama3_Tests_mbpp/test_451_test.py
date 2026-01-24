import unittest
from mbpp_451_code import remove_whitespaces

class TestRemoveWhitespaces(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(remove_whitespaces("Hello World"), "HelloWorld")

    def test_multiple_spaces(self):
        self.assertEqual(remove_whitespaces("Hello   World"), "HelloWorld")

    def test_single_space(self):
        self.assertEqual(remove_whitespaces("Hello World"), "HelloWorld")

    def test_multiple_lines(self):
        self.assertEqual(remove_whitespaces("Hello\nWorld"), "HelloWorld")

    def test_empty_input(self):
        self.assertEqual(remove_whitespaces(""), "")

    def test_single_space_at_end(self):
        self.assertEqual(remove_whitespaces("Hello World "), "HelloWorld")

    def test_multiple_spaces_at_end(self):
        self.assertEqual(remove_whitespaces("Hello World   "), "HelloWorld")

    def test_multiple_spaces_and_lines(self):
        self.assertEqual(remove_whitespaces("Hello\n   World"), "HelloWorld")
