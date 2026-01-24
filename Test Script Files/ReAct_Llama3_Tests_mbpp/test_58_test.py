import unittest
from mbpp_58_code import opposite_Signs

class TestOppositeSigns(unittest.TestCase):

    def test_positive_positive(self):
        self.assertFalse(opposite_Signs(5, 5))

    def test_negative_negative(self):
        self.assertFalse(opposite_Signs(-5, -5))

    def test_positive_negative(self):
        self.assertTrue(opposite_Signs(5, -5))

    def test_negative_positive(self):
        self.assertTrue(opposite_Signs(-5, 5))

    def test_zero_zero(self):
        self.assertFalse(opposite_Signs(0, 0))

    def test_zero_nonzero(self):
        self.assertTrue(opposite_Signs(0, 5))

    def test_nonzero_zero(self):
        self.assertTrue(opposite_Signs(5, 0))

    def test_nonzero_nonzero(self):
        self.assertFalse(opposite_Signs(5, 5))
