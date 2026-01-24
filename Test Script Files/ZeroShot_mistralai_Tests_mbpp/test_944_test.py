import unittest
from mbpp_944_code import num_position

class TestNumPosition(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(num_position(""), -1)

    def test_single_digit(self):
        self.assertEqual(num_position("1"), 0)

    def test_multiple_digits(self):
        self.assertEqual(num_position("12345"), 0)

    def test_multiple_words_single_digit(self):
        self.assertEqual(num_position("hello 1 world"), 6)

    def test_multiple_words_multiple_digits(self):
        self.assertEqual(num_position("apple 12 banana 45 cherry 67"), 6)

    def test_leading_digits(self):
        self.assertEqual(num_position("1hello world"), 0)

    def test_trailing_digits(self):
        self.assertEqual(num_position("world 1"), 4)

    def test_digits_in_middle(self):
        self.assertEqual(num_position("hello 123 world"), 3)

    def test_digits_with_special_characters(self):
        self.assertEqual(num_position("hello$123world"), 4)

    def test_digits_with_punctuation(self):
        self.assertEqual(num_position("hello,123 world."), 5)
