import unittest
from mbpp_908_code import find_fixed_point

class TestFindFixedPoint(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(find_fixed_point([0, 1, 2, 3, 4], 4), 4)
        self.assertEqual(find_fixed_point([5, 4, 3, 2, 1], 5), -1)
        self.assertEqual(find_fixed_point([1, 1, 2, 3, 4], 4), 1)

    def test_edge_and_boundary(self):
        self.assertEqual(find_fixed_point([], 0), -1)
        self.assertEqual(find_fixed_point([0], 1), -1)
        self.assertEqual(find_fixed_point([0, 1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(find_fixed_point([0, 1, 2, 3, 4, 5], 7), -1)

    def test_complex_cases(self):
        self.assertEqual(find_fixed_point([1, 2, 3, 4, 5, 6, 7, 6, 5], 9), 5)
        self.assertEqual(find_fixed_point([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0], 11), 0)
        self.assertEqual(find_fixed_point([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 0, 1], 14), 1)
