import unittest
from mbpp_58_code import opposite_Signs

class TestOppositeSigns(unittest.TestCase):
    def test_simple_positive(self):
        self.assertTrue(opposite_Signs(1, 1))

    def test_simple_negative(self):
        self.assertFalse(opposite_Signs(-1, -1))

    def test_edge_zero(self):
        self.assertFalse(opposite_Signs(0, 0))

    def test_edge_negative_positive(self):
        self.assertTrue(opposite_Signs(-1, 1))

    def test_edge_positive_negative(self):
        self.assertTrue(opposite_Signs(1, -1))

    def test_edge_zero_positive(self):
        self.assertFalse(opposite_Signs(0, 1))

    def test_edge_zero_negative(self):
        self.assertFalse(opposite_Signs(0, -1))

    def test_edge_negative_zero(self):
        self.assertTrue(opposite_Signs(-1, 0))

    def test_edge_positive_zero(self):
        self.assertTrue(opposite_Signs(1, 0))

    def test_edge_negative_negative(self):
        self.assertFalse(opposite_Signs(-1, -1))

    def test_edge_positive_positive(self):
        self.assertFalse(opposite_Signs(1, 1))

    def test_edge_zero_zero(self):
        self.assertFalse(opposite_Signs(0, 0))
