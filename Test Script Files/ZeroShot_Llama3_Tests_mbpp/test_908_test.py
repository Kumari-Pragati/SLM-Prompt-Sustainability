import unittest
from mbpp_908_code import find_fixed_point

class TestFindFixedPoint(unittest.TestCase):

    def test_find_fixed_point(self):
        self.assertEqual(find_fixed_point([0, 1, 2, 3, 4, 5, 2, 3, 4, 2, 3, 4], 11), 2)
        self.assertEqual(find_fixed_point([-1, 0, 2, 3, 4, 5, 2, 3, 4, 2, 3, 4], 11), 0)
        self.assertEqual(find_fixed_point([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 12), -1)
        self.assertEqual(find_fixed_point([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 12), 0)
        self.assertEqual(find_fixed_point([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12], 12), -1)
