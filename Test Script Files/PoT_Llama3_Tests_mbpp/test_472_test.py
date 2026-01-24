import unittest
from mbpp_472_code import check_Consecutive

class TestCheckConsecutive(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_Consecutive([1, 2, 3, 4, 5]))

    def test_edge_case_empty_list(self):
        self.assertFalse(check_Consecutive([]))

    def test_edge_case_single_element_list(self):
        self.assertTrue(check_Consecutive([1]))

    def test_edge_case_single_element_list_with_duplicates(self):
        self.assertFalse(check_Consecutive([1, 1]))

    def test_edge_case_consecutive_range(self):
        self.assertTrue(check_Consecutive([1, 2, 3, 4, 5, 6]))

    def test_edge_case_non_consecutive_range(self):
        self.assertFalse(check_Consecutive([1, 3, 5]))

    def test_edge_case_consecutive_range_with_duplicates(self):
        self.assertTrue(check_Consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]))

    def test_edge_case_non_consecutive_range_with_duplicates(self):
        self.assertFalse(check_Consecutive([1, 1, 2, 2, 3, 3, 5]))

    def test_edge_case_consecutive_range_with_negative_numbers(self):
        self.assertTrue(check_Consecutive([-5, -4, -3, -2, -1]))

    def test_edge_case_non_consecutive_range_with_negative_numbers(self):
        self.assertFalse(check_Consecutive([-5, -3, -1]))

    def test_edge_case_consecutive_range_with_negative_and_positive_numbers(self):
        self.assertTrue(check_Consecutive([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]))

    def test_edge_case_non_consecutive_range_with_negative_and_positive_numbers(self):
        self.assertFalse(check_Consecutive([-5, -3, 0, 1, 2, 3, 5]))
