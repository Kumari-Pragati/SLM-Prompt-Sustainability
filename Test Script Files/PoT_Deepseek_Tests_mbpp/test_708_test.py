import unittest
from mbpp_708_code import Convert

class TestConvertFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Convert("Hello World"), ["Hello", "World"])

    def test_empty_string(self):
        self.assertEqual(Convert(""), [])

    def test_single_word(self):
        self.assertEqual(Convert("Python"), ["Python"])

    def test_multiple_spaces(self):
        self.assertEqual(Convert("   Hello     World   "), ["Hello", "World"])

    def test_no_spaces(self):
        self.assertEqual(Convert("HelloWorld"), ["HelloWorld"])

    def test_special_characters(self):
        self.assertEqual(Convert("Hello@World"), ["Hello@World"])

    def test_numbers_in_string(self):
        self.assertEqual(Convert("Hello123World"), ["Hello123World"])
