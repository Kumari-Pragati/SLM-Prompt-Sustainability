import unittest
from mbpp_908_code import find_fixed_point

class TestFindFixedPoint(unittest.TestCase):

    def test_found_fixed_point(self):
        self.assertEqual(find_fixed_point([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10), 0)

    def test_not_found_fixed_point(self):
        self.assertEqual(find_fixed_point([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), -1)

    def test_edge_case_empty_array(self):
        self.assertEqual(find_fixed_point([], 0), -1)

    def test_edge_case_single_element_array(self):
        self.assertEqual(find_fixed_point([0], 1), 0)

    def test_edge_case_array_with_duplicates(self):
        self.assertEqual(find_fixed_point([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 11), 0)

    def test_edge_case_array_with_duplicates_and_not_found(self):
        self.assertEqual(find_fixed_point([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11), -1)
