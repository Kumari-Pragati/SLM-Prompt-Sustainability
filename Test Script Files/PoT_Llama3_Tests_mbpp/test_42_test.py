import unittest
from mbpp_42_code import find_Sum

class TestFindSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 5), 9)

    def test_edge_case_single_element(self):
        self.assertEqual(find_Sum([1], 1), 1)

    def test_edge_case_empty_list(self):
        self.assertEqual(find_Sum([], 0), 0)

    def test_edge_case_single_element_repeated(self):
        self.assertEqual(find_Sum([1, 1], 2), 2)

    def test_edge_case_empty_list_with_n(self):
        self.assertEqual(find_Sum([], 5), 0)

    def test_edge_case_single_element_repeated_with_n(self):
        self.assertEqual(find_Sum([1, 1, 1, 1, 1], 5), 5)

    def test_edge_case_list_with_duplicates(self):
        self.assertEqual(find_Sum([1, 2, 2, 3, 3, 3], 6), 6)

    def test_edge_case_list_with_duplicates_and_n(self):
        self.assertEqual(find_Sum([1, 2, 2, 3, 3, 3], 6), 6)
