import unittest
from mbpp_58_code import opposite_Signs

class TestOppositeSigns(unittest.TestCase):
    def test_positive_and_positive(self):
        self.assertFalse(opposite_Signs(1, 1))

    def test_negative_and_negative(self):
        self.assertFalse(opposite_Signs(-1, -1))

    def test_positive_and_negative(self):
        self.assertTrue(opposite_Signs(1, -1))

    def test_negative_and_positive(self):
        self.assertTrue(opposite_Signs(-1, 1))

    def test_zero_and_zero(self):
        self.assertFalse(opposite_Signs(0, 0))

    def test_zero_and_nonzero(self):
        self.assertTrue(opposite_Signs(0, 1))

    def test_nonzero_and_zero(self):
        self.assertTrue(opposite_Signs(1, 0))
