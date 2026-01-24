import unittest
from mbpp_42_code import find_Sum

class TestFindSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Sum([1, 2, 2, 3, 4, 4, 5]), 4)

    def test_edge_case_single_element(self):
        self.assertEqual(find_Sum([1]), 1)

    def test_edge_case_no_duplicates(self):
        self.assertEqual(find_Sum([1, 2, 3, 4]), 0)

    def test_corner_case_empty_list(self):
        self.assertEqual(find_Sum([]), 0)

    def test_corner_case_single_element_list(self):
        self.assertEqual(find_Sum([1]), 1)

    def test_corner_case_all_duplicates(self):
        self.assertEqual(find_Sum([1, 1, 1]), 1)
