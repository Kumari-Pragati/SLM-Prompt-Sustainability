import unittest
from mbpp_204_code import count

class TestCount(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count("", "a"), 0)

    def test_single_character(self):
        self.assertEqual(count("a", "a"), 1)

    def test_multiple_characters(self):
        self.assertEqual(count("abcdefg", "a"), 3)

    def test_case_insensitive(self):
        self.assertEqual(count("ABC", "c"), 1)

    def test_negative_input(self):
        self.assertRaises(ValueError, count, "", "-")

    def test_non_string_input(self):
        self.assertRaises(TypeError, count, [1, 2, 3], "a")
