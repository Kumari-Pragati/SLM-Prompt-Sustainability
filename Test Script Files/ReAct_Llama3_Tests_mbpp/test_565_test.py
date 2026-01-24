import unittest
from mbpp_565_code import split

class TestSplitFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(split("hello"), ["h", "e", "l", "l", "o"])

    def test_empty_string(self):
        self.assertEqual(split(""), [])

    def test_single_character(self):
        self.assertEqual(split("a"), ["a"])

    def test_multiple_characters(self):
        self.assertEqual(split("abc"), ["a", "b", "c"])

    def test_long_string(self):
        self.assertEqual(split("abcdefghijklmnopqrstuvwxyz"), list(range(26)))

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            split(123)

    def test_non_string_input_with_message(self):
        with self.assertRaises(TypeError) as e:
            split(123)
        self.assertEqual(str(e.exception), "'word' must be a string")
