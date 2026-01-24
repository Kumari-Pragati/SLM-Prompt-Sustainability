import unittest
from mbpp_678_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):
    def test_simple_string(self):
        self.assertEqual(remove_spaces("Hello World"), "HelloWorld")

    def test_empty_string(self):
        self.assertEqual(remove_spaces(""), "")

    def test_single_space(self):
        self.assertEqual(remove_spaces(" "), "")

    def test_multiple_spaces(self):
        self.assertEqual(remove_spaces("Hello   World"), "HelloWorld")

    def test_special_characters(self):
        self.assertEqual(remove_spaces("Hello@World"), "Hello@World")

    def test_leading_trailing_spaces(self):
        self.assertEqual(remove_spaces(" Hello World "), "HelloWorld")

    def test_punctuation_spaces(self):
        self.assertEqual(remove_spaces("Hello, World!"), "HelloWorld")
