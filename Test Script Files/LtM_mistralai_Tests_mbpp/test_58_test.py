import unittest
from mbpp_58_code import opposite_Signs

class TestOppositeSigns(unittest.TestCase):

    def test_simple_positive(self):
        self.assertFalse(opposite_Signs(1, 1))

    def test_simple_negative(self):
        self.assertTrue(opposite_Signs(-1, 1))

    def test_simple_zero(self):
        self.assertFalse(opposite_Signs(0, 0))

    def test_edge_cases_positive(self):
        self.assertFalse(opposite_Signs(2147483647, 0))
        self.assertFalse(opposite_Signs(0, 2147483647))

    def test_edge_cases_negative(self):
        self.assertTrue(opposite_Signs(-2147483648, -1))
        self.assertTrue(opposite_Signs(-1, -2147483648))

    def test_edge_case_zero(self):
        self.assertFalse(opposite_Signs(0, 0))

    def test_combined_cases(self):
        self.assertTrue(opposite_Signs(-1, 1))
        self.assertTrue(opposite_Signs(1, -1))
        self.assertFalse(opposite_Signs(1, 1))
        self.assertFalse(opposite_Signs(-1, -1))
