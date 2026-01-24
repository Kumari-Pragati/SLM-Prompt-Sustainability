import unittest
from mbpp_58_code import opposite_Signs

class TestOppositeSigns(unittest.TestCase):
    def test_normal_inputs(self):
        self.assertTrue(opposite_Signs(-5, 5))
        self.assertTrue(opposite_Signs(5, -5))

    def test_edge_and_boundary_conditions(self):
        self.assertFalse(opposite_Signs(0, 0))
        self.assertTrue(opposite_Signs(-1, 1))
        self.assertTrue(opposite_Signs(1, -1))
        self.assertFalse(opposite_Signs(5, 5))
        self.assertFalse(opposite_Signs(-5, -5))

    def test_negative_numbers(self):
        self.assertTrue(opposite_Signs(-5, -3))
        self.assertTrue(opposite_Signs(-3, -5))

    def test_positive_numbers(self):
        self.assertTrue(opposite_Signs(3, 5))
        self.assertTrue(opposite_Signs(5, 3))

    def test_mixed_inputs(self):
        self.assertTrue(opposite_Signs(-5, 3))
        self.assertTrue(opposite_Signs(3, -5))
