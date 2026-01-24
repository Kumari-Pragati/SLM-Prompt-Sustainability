import unittest
from mbpp_204_code import count

class TestCountFunction(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count("", "a"), 0)

    def test_single_character(self):
        self.assertEqual(count("a", "a"), 1)
        self.assertEqual(count("A", "a"), 0)

    def test_multiple_characters(self):
        self.assertEqual(count("abc", "a"), 1)
        self.assertEqual(count("abc", "b"), 1)
        self.assertEqual(count("abc", "c"), 1)

    def test_case_sensitivity(self):
        self.assertEqual(count("ABC", "a"), 0)
        self.assertEqual(count("abc", "A"), 0)

    def test_long_string(self):
        long_string = "x" * 1000
        self.assertEqual(count(long_string, "x"), 1000)

    def test_negative_index(self):
        self.assertRaises(IndexError, lambda: count("-1", "a"))

    def test_string_with_non_string_input(self):
        self.assertRaises(TypeError, lambda: count("123", 4))
