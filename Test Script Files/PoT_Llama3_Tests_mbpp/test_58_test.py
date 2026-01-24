import unittest
from mbpp_58_code import opposite_Signs

class TestOppositeSigns(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(opposite_Signs(1, 1))
        self.assertFalse(opposite_Signs(1, -1))
        self.assertTrue(opposite_Signs(-1, 1))
        self.assertFalse(opposite_Signs(-1, -1))

    def test_edge_cases(self):
        self.assertFalse(opposite_Signs(0, 0))
        self.assertTrue(opposite_Signs(0, 1))
        self.assertTrue(opposite_Signs(0, -1))

    def test_corner_cases(self):
        self.assertFalse(opposite_Signs(1, 0))
        self.assertFalse(opposite_Signs(-1, 0))
