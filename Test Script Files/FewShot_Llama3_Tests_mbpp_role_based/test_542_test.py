import unittest
from mbpp_542_code import fill_spaces

class TestFillSpaces(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(fill_spaces("Hello, world!"), "Hello:world:")

    def test_multiple_spaces(self):
        self.assertEqual(fill_spaces("Hello   world!"), "Hello:world:")

    def test_multiple_punctuation(self):
        self.assertEqual(fill_spaces("Hello, world!"), "Hello:world:")

    def test_empty_string(self):
        self.assertEqual(fill_spaces(""), "")

    def test_single_character(self):
        self.assertEqual(fill_spaces("a"), "a")

    def test_long_string(self):
        long_string = "Hello, world! This is a test string."
        self.assertEqual(fill_spaces(long_string), "Hello:world!:This:is:a:test:string.")
