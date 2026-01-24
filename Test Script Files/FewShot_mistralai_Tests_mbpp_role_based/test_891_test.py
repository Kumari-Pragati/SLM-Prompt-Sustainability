import unittest
from mbpp_891_code import same_Length

class TestSameLength(unittest.TestCase):
    def test_same_length_positive_numbers(self):
        self.assertTrue(same_Length(1234, 5678))
        self.assertTrue(same_Length(9876, 1234))

    def test_same_length_zero(self):
        self.assertTrue(same_Length(0, 0))

    def test_different_length_positive_numbers(self):
        self.assertFalse(same_Length(1234, 567))
        self.assertFalse(same_Length(9876, 123))

    def test_negative_numbers(self):
        self.assertTrue(same_Length(-1234, -5678))
        self.assertTrue(same_Length(-9876, -1234))

    def test_mixed_signs(self):
        self.assertFalse(same_Length(-1234, 5678))
        self.assertFalse(same_Length(1234, -5678))
