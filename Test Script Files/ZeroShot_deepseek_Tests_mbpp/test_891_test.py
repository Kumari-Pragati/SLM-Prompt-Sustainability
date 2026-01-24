import unittest
from mbpp_891_code import same_Length

class TestSameLength(unittest.TestCase):

    def test_same_length_positive_numbers(self):
        self.assertTrue(same_Length(123, 456))
        self.assertTrue(same_Length(789, 12345))

    def test_same_length_negative_numbers(self):
        self.assertTrue(same_Length(-123, -456))
        self.assertTrue(same_Length(-789, -12345))

    def test_same_length_zero(self):
        self.assertTrue(same_Length(0, 0))

    def test_same_length_different_lengths(self):
        self.assertFalse(same_Length(123, 1234))
        self.assertFalse(same_Length(456, 78))

    def test_same_length_with_decimal_numbers(self):
        self.assertFalse(same_Length(123.45, 67.89))
