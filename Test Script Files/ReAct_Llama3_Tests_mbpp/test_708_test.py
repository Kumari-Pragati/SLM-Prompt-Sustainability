import unittest
from mbpp_708_code import Convert

class TestConvert(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(Convert(""), [])

    def test_single_word(self):
        self.assertEqual(Convert("hello"), ["hello"])

    def test_multiple_words(self):
        self.assertEqual(Convert("hello world"), ["hello", "world"])

    def test_multiple_spaces(self):
        self.assertEqual(Convert("hello   world"), ["hello", "world"])

    def test_leading_trailing_spaces(self):
        self.assertEqual(Convert("   hello   world   "), ["hello", "world"])

    def test_empty_string_with_spaces(self):
        self.assertEqual(Convert("   "), [])

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            Convert(123)
