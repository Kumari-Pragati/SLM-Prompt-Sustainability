import unittest
from mbpp_908_code import find_fixed_point

class TestFindFixedPoint(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_fixed_point([], 1), -1)

    def test_single_element_list(self):
        self.assertEqual(find_fixed_point([0], 1), 0)
        self.assertEqual(find_fixed_point([1], 1), 1)

    def test_fixed_point_present(self):
        self.assertEqual(find_fixed_point([0, 1, 2, 0], 4), 2)
        self.assertEqual(find_fixed_point([3, 0, 1, 5, 2, 3, 4, 2, 0, 4, 5], 12), 10)

    def test_fixed_point_not_present(self):
        self.assertEqual(find_fixed_point([1, 2, 3, 4], 4), -1)
