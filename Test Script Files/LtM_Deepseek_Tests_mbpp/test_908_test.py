import unittest
from mbpp_908_code import find_fixed_point

class TestFindFixedPoint(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_fixed_point([0, 2, 3, 4], 4), 0)
        self.assertEqual(find_fixed_point([-10, -5, 0, 3, 7], 5), 3)

    def test_edge_conditions(self):
        self.assertEqual(find_fixed_point([], 0), -1)
        self.assertEqual(find_fixed_point([1, 2, 3, 4], 4), -1)
        self.assertEqual(find_fixed_point([-1, -2, -3, -4], 4), -1)

    def test_complex_cases(self):
        self.assertEqual(find_fixed_point([-1, 0, 1, 2, 3], 5), 1)
        self.assertEqual(find_fixed_point([1, 1, 1, 1, 1], 5), 0)
        self.assertEqual(find_fixed_point([-1, -2, -3, -4, -5], 5), -1)
