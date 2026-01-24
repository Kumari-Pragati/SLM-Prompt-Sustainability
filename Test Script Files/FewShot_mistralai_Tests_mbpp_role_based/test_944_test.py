import unittest
from mbpp_944_code import num_position

class TestNumPosition(unittest.TestCase):
    def test_single_digit(self):
        self.assertEqual(num_position("1"), 0)

    def test_multiple_digits(self):
        self.assertEqual(num_position("12345"), 0)

    def test_multiple_words_single_number(self):
        self.assertEqual(num_position("Hello 123 World"), 4)

    def test_multiple_numbers(self):
        self.assertEqual(num_position("123 456 789"), 0)

    def test_empty_string(self):
        self.assertIsNone(num_position(""))

    def test_no_numbers(self):
        self.assertIsNone(num_position("abcdefg"))

    def test_leading_numbers(self):
        self.assertEqual(num_position("123abc"), 0)

    def test_trailing_numbers(self):
        self.assertEqual(num_position("abc123"), len("abc123") - 1)

    def test_numbers_in_middle(self):
        self.assertEqual(num_position("ab1c2d3"), 1)
