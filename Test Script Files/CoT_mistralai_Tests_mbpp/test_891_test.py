import unittest
from mbpp_891_code import same_Length

class TestSameLength(unittest.TestCase):
    def test_same_length_positive_integers(self):
        self.assertTrue(same_Length(1234, 5678))
        self.assertTrue(same_Length(9999, 9999))
        self.assertTrue(same_Length(123, 456))

    def test_same_length_zero(self):
        self.assertTrue(same_Length(0, 0))

    def test_same_length_negative_integers(self):
        self.assertTrue(same_Length(-1234, -5678))
        self.assertTrue(same_Length(-9999, -9999))
        self.assertTrue(same_Length(-123, -456))

    def test_different_lengths(self):
        self.assertFalse(same_Length(1234, 567))
        self.assertFalse(same_Length(1234, 56789))
        self.assertFalse(same_Length(123, 4567))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, same_Length, "123", 456)
        self.assertRaises(TypeError, same_Length, 123, "456")
