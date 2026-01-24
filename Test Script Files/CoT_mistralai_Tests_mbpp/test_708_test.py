import unittest
from mbpp_708_code import Convert

class TestConvert(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(Convert(""), [])

    def test_single_word(self):
        self.assertEqual(Convert("hello"), ["hello"])

    def test_multiple_words(self):
        self.assertEqual(Convert("hello world"), ["hello", "world"])

    def test_whitespace_only(self):
        self.assertEqual(Convert("   "), [""])

    def test_leading_trailing_whitespace(self):
        self.assertEqual(Convert(" hello world "), ["hello", "world"])

    def test_punctuation(self):
        self.assertEqual(Convert("hello, world!"), ["hello", "world"])

    def test_numbers(self):
        self.assertEqual(Convert("1 2 3"), ["1", "2", "3"])

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            Convert("hello, 1, world!, 3.14")
