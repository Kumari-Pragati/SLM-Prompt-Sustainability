import unittest
from mbpp_58_code import opposite_Signs

class TestOppositeSigns(unittest.TestCase):

    def test_opposite_signs_positive_numbers(self):
        self.assertFalse(opposite_Signs(5, 3))
        self.assertFalse(opposite_Signs(10, 20))

    def test_opposite_signs_negative_numbers(self):
        self.assertTrue(opposite_Signs(-5, -3))
        self.assertTrue(opposite_Signs(-10, -20))

    def test_opposite_signs_zero(self):
        self.assertFalse(opposite_Signs(0, 5))
        self.assertFalse(opposite_Signs(5, 0))

    def test_opposite_signs_mixed_numbers(self):
        self.assertTrue(opposite_Signs(-5, 3))
        self.assertTrue(opposite_Signs(5, -3))
        self.assertFalse(opposite_Signs(0, 0))
