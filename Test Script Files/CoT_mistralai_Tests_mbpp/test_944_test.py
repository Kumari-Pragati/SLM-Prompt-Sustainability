import unittest
from mbpp_944_code import num_position

class TestNumPosition(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(num_position(""), -1)

    def test_single_digit(self):
        self.assertEqual(num_position("1"), 0)
        self.assertEqual(num_position("9"), 0)

    def test_multiple_digits(self):
        self.assertEqual(num_position("12345"), 0)
        self.assertEqual(num_position("98765"), 4)

    def test_multiple_words_single_digit(self):
        self.assertEqual(num_position("hello1world"), 5)
        self.assertEqual(num_position("world1hello"), 0)

    def test_multiple_words_multiple_digits(self):
        self.assertEqual(num_position("hello12world34"), 0)
        self.assertEqual(num_position("world34hello12"), 5)

    def test_leading_zero(self):
        self.assertEqual(num_position("01"), 0)
        self.assertEqual(num_position("001"), 2)

    def test_trailing_zero(self):
        self.assertEqual(num_position("10"), 0)
        self.assertEqual(num_position("100"), 2)

    def test_leading_and_trailing_zero(self):
        self.assertEqual(num_position("010"), 1)
        self.assertEqual(num_position("0100"), 2)

    def test_leading_and_trailing_spaces(self):
        self.assertEqual(num_position(" 1 "), 1)
        self.assertEqual(num_position(" 123 "), 1)

    def test_non_numeric_characters(self):
        self.assertEqual(num_position("1a2b3"), -1)
        self.assertEqual(num_position("123a"), -1)
        self.assertEqual(num_position("123ab"), -1)
