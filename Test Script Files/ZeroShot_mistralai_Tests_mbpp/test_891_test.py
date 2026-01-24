import unittest
from mbpp_891_code import same_Length

class TestSameLength(unittest.TestCase):

    def test_same_length_positive(self):
        self.assertTrue(same_Length(1234, 5678))
        self.assertTrue(same_Length(0.0123, 0.4567))
        self.assertTrue(same_Length(123456789, 1234567890))

    def test_same_length_zero(self):
        self.assertTrue(same_Length(0, 0))
        self.assertTrue(same_Length(0.0, 0.0))

    def test_same_length_negative(self):
        self.assertFalse(same_Length(1234, -5678))
        self.assertFalse(same_Length(-0.0123, 0.4567))
        self.assertFalse(same_Length(123456789, -1234567890))

    def test_same_length_one_zero(self):
        self.assertFalse(same_Length(1234, 0))
        self.assertFalse(same_Length(0, 1234))
        self.assertFalse(same_Length(0.0123, 0))
        self.assertFalse(same_Length(0, 0.0123))
