import unittest
from mbpp_708_code import Convert

class TestConvert(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(Convert("Hello World"), ["Hello", "World"])

    def test_empty_string(self):
        self.assertEqual(Convert(""), [])

    def test_single_word(self):
        self.assertEqual(Convert("Python"), ["Python"])

    def test_multiple_spaces(self):
        self.assertEqual(Convert("Hello   World"), ["Hello", "World"])

    def test_trailing_spaces(self):
        self.assertEqual(Convert("Hello World   "), ["Hello", "World"])

    def test_leading_spaces(self):
        self.assertEqual(Convert("   Hello World"), ["Hello", "World"])

    def test_mixed_spaces(self):
        self.assertEqual(Convert("   Hello   World   "), ["Hello", "World"])
