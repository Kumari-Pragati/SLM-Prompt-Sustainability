import unittest
from mbpp_908_code import find_fixed_point

class TestFindFixedPoint(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_fixed_point([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10), 5)
        self.assertEqual(find_fixed_point([10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 10), -1)
        self.assertEqual(find_fixed_point([0, 1, 2, 3, 4, 4, 6, 7, 8, 9], 10), 4)
        self.assertEqual(find_fixed_point([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8], 10), -1)
        self.assertEqual(find_fixed_point([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9], 11), 9)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(find_fixed_point([], 0), -1)
        self.assertEqual(find_fixed_point([0], 1), -1)
        self.assertEqual(find_fixed_point([0, 1], 2), -1)
        self.assertEqual(find_fixed_point([0, 1, 2], 3), -1)
        self.assertEqual(find_fixed_point([0, 1, 2, 3], 4), -1)
        self.assertEqual(find_fixed_point([0, 1, 2, 3, 4], 5), -1)
        self.assertEqual(find_fixed_point([0, 1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(find_fixed_point([0, 1, 2, 3, 4, 5, 6], 7), -1)
        self.assertEqual(find_fixed_point([0, 1, 2, 3, 4, 5, 6, 7], 8), -1)
        self.assertEqual(find_fixed_point([0, 1, 2, 3, 4, 5, 6, 7, 8], 9), -1)
        self.assertEqual(find_fixed_point([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10), 9)
        self.assertEqual(find_fixed_point([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11), -1)
