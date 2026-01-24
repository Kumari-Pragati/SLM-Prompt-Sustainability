import unittest
from mbpp_891_code import same_Length

class TestSameLength(unittest.TestCase):
    def test_same_length_positive_numbers(self):
        self.assertTrue(same_Length(123, 456))
        self.assertTrue(same_Length(999, 999))
        self.assertFalse(same_Length(123, 457))

    def test_same_length_zero(self):
        self.assertTrue(same_Length(0, 0))

    def test_same_length_negative_numbers(self):
        self.assertTrue(same_Length(-123, -456))
        self.assertTrue(same_Length(-999, -999))
        self.assertFalse(same_Length(-123, -457))

    def test_same_length_mixed_signs(self):
        self.assertFalse(same_Length(-123, 456))
        self.assertFalse(same_Length(123, -456))

    def test_same_length_one_zero(self):
        self.assertFalse(same_Length(123, 0))
        self.assertFalse(same_Length(0, 123))
