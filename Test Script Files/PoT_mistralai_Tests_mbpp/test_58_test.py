import unittest
from mbpp_58_code import opposite_Signs

class TestOppositeSigns(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(opposite_Signs(1, -1))
        self.assertTrue(opposite_Signs(-1, 1))
        self.assertFalse(opposite_Signs(0, 0))
        self.assertFalse(opposite_Signs(1, 1))
        self.assertFalse(opposite_Signs(-1, -1))

    def test_edge_and_boundary_cases(self):
        self.assertTrue(opposite_Signs(float('inf'), -float('inf')))
        self.assertTrue(opposite_Signs(-float('inf'), float('inf')))
        self.assertFalse(opposite_Signs(float('nan'), float('nan')))
        self.assertFalse(opposite_Signs(float('inf'), 0))
        self.assertFalse(opposite_Signs(-float('inf'), 0))
