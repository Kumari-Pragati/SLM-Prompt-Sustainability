import unittest
from mbpp_708_code import Convert

class TestConvertFunction(unittest.TestCase):

    def test_simple_string(self):
        self.assertEqual(Convert("Hello World"), ["Hello", "World"])

    def test_empty_string(self):
        self.assertEqual(Convert(""), [])

    def test_string_with_single_word(self):
        self.assertEqual(Convert("Python"), ["Python"])

    def test_string_with_multiple_spaces(self):
        self.assertEqual(Convert("   Hello     World   "), ["Hello", "World"])

    def test_string_with_special_characters(self):
        self.assertEqual(Convert("Hello@World"), ["Hello@World"])
