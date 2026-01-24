import unittest
from mbpp_908_code import find_fixed_point

class TestFindFixedPoint(unittest.TestCase):
    def test_found_fixed_point(self):
        self.assertEqual(find_fixed_point([0, 1, 2, 0], 4), 2)
        self.assertEqual(find_fixed_point([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1], 12), 1)

    def test_not_found_fixed_point(self):
        self.assertEqual(find_fixed_point([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10), -1)

    def test_empty_list(self):
        self.assertEqual(find_fixed_point([], 0), -1)

    def test_negative_index(self):
        self.assertEqual(find_fixed_point([0, 1, 2], -1), -1)

    def test_negative_number(self):
        self.assertEqual(find_fixed_point([-1, -2, -3], 3), -1)
