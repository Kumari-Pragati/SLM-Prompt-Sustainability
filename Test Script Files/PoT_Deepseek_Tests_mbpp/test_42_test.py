import unittest
from mbpp_42_code import find_Sum

class TestFindSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Sum([1, 2, 3, 2, 1], 5), 4)

    def test_edge_case_single_element(self):
        self.assertEqual(find_Sum([1], 1), 0)

    def test_edge_case_empty_list(self):
        self.assertEqual(find_Sum([], 0), 0)

    def test_boundary_case_repeated_elements(self):
        self.assertEqual(find_Sum([1, 1, 1, 1], 4), 4)

    def test_corner_case_no_repeated_elements(self):
        self.assertEqual(find_Sum([1, 2, 3, 4], 4), 0)

    def test_corner_case_all_repeated_elements(self):
        self.assertEqual(find_Sum([1, 1, 1, 1, 1], 5), 5)
