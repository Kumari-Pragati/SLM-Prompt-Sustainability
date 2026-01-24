import unittest
from mbpp_908_code import find_fixed_point

class TestFindFixedPoint(unittest.TestCase):

    def test_find_fixed_point_normal(self):
        self.assertEqual(find_fixed_point([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 9)
        self.assertEqual(find_fixed_point([10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 19), 19)
        self.assertEqual(find_fixed_point([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8], 8), -1)

    def test_find_fixed_point_edge_cases(self):
        self.assertEqual(find_fixed_point([0], 0), -1)
        self.assertEqual(find_fixed_point([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), -1)
        self.assertEqual(find_fixed_point([], 0), -1)
        self.assertEqual(find_fixed_point([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 11), -1)

    def test_find_fixed_point_invalid_input(self):
        self.assertRaises(TypeError, find_fixed_point, [1, 2, 3], 'invalid')
        self.assertRaises(TypeError, find_fixed_point, [1, 2, 3], 1.5)
