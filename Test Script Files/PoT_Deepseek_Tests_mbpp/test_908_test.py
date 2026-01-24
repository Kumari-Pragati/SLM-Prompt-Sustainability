import unittest
from mbpp_908_code import find_fixed_point

class TestFindFixedPoint(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_fixed_point([0, 2, 3, 4], 4), 0)

    def test_edge_case_empty_array(self):
        self.assertEqual(find_fixed_point([], 0), -1)

    def test_boundary_case_single_element(self):
        self.assertEqual(find_fixed_point([0], 1), 0)
        self.assertEqual(find_fixed_point([1], 1), -1)

    def test_corner_case_negative_numbers(self):
        self.assertEqual(find_fixed_point([-1, -2, -3, -4], 4), -1)

    def test_corner_case_large_numbers(self):
        self.assertEqual(find_fixed_point([100000, 199999, 299998, 399997], 4), -1)

    def test_corner_case_duplicates(self):
        self.assertEqual(find_fixed_point([0, 1, 1, 3], 4), 1)
