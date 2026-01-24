import unittest
from mbpp_232_code import larg_nnum

class TestLargNnum(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(larg_nnum([1, 2, 3, 4, 5], 3), [5, 4, 3])

    def test_edge_boundary_conditions(self):
        self.assertEqual(larg_nnum([], 3), [])
        self.assertEqual(larg_nnum([1], 3), [])
        self.assertEqual(larg_nnum([1, 2, 3, 4, 5], 0), [])
        self.assertEqual(larg_nnum([1, 2, 3, 4, 5], 6), [5, 4, 3, 2, 1])

    def test_more_complex_cases(self):
        self.assertEqual(larg_nnum([10, 4, 9, 1, 7], 2), [10, 9])
        self.assertEqual(larg_nnum([1, 1, 1, 1, 1], 5), [1, 1, 1, 1, 1])
        self.assertEqual(larg_nnum([-1, -2, -3, -4, -5], 3), [-1, -2, -3])
