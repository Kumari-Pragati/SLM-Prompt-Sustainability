import unittest
from mbpp_700_code import count_range_in_list

class TestCountRangeInList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 2, 4), 3)

    def test_edge_case_min(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 1, 4), 4)

    def test_edge_case_max(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 2, 5), 4)

    def test_boundary_case_min_max(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 1, 5), 5)

    def test_corner_case_empty_list(self):
        self.assertEqual(count_range_in_list([], 1, 5), 0)

    def test_corner_case_single_element_in_range(self):
        self.assertEqual(count_range_in_list([3], 2, 4), 1)

    def test_corner_case_single_element_out_of_range(self):
        self.assertEqual(count_range_in_list([3], 1, 2), 0)

    def test_corner_case_all_elements_out_of_range(self):
        self.assertEqual(count_range_in_list([1, 2, 4, 5], 3, 6), 0)
