import unittest
from mbpp_899_code import check

class TestCheckFunction(unittest.TestCase):

    def test_simple_valid_inputs(self):
        self.assertTrue(check([1, 2, 3, 4, 5], 5))
        self.assertTrue(check([5, 4, 3, 2, 1], 5))
        self.assertTrue(check([1, 2, 2, 2, 1], 5))

    def test_edge_and_boundary_conditions(self):
        self.assertTrue(check([1], 1))
        self.assertTrue(check([], 0))
        self.assertTrue(check([1, 1, 1, 1, 1], 5))
        self.assertTrue(check([2, 2, 2, 2, 2], 5))

    def test_more_complex_or_corner_cases(self):
        self.assertFalse(check([1, 2, 3, 2, 1], 5))
        self.assertFalse(check([5, 4, 5, 4, 5], 5))
        self.assertFalse(check([-1, 0, 1, 0, -1], 5))
        self.assertFalse(check([1, 2, 3, 4, 5, 6], 6))
