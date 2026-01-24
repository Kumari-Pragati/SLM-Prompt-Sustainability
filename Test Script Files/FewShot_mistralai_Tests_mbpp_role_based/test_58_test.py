import unittest
from mbpp_58_code import opposite_Signs

class TestOppositeSigns(unittest.TestCase):
    def test_positive_and_negative(self):
        self.assertTrue(opposite_Signs(-1, 1))
        self.assertTrue(opposite_Signs(1, -1))

    def test_same_sign(self):
        self.assertFalse(opposite_Signs(1, 1))
        self.assertFalse(opposite_Signs(-1, -1))

    def test_zero(self):
        self.assertFalse(opposite_Signs(0, 0))
