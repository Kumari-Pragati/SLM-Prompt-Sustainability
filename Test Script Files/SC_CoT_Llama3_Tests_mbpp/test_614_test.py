import unittest
from mbpp_614_code import cummulative_sum

class TestCummulativeSum(unittest.TestCase):

    def test_typical_input(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(cummulative_sum(test_list), 45)

    def test_edge_case_empty_list(self):
        test_list = []
        self.assertEqual(cummulative_sum(test_list), 0)

    def test_edge_case_single_element_list(self):
        test_list = [[1, 2, 3]]
        self.assertEqual(cummulative_sum(test_list), 6)

    def test_edge_case_single_element_list_with_single_element_sublist(self):
        test_list = [[1], [2], [3]]
        self.assertEqual(cummulative_sum(test_list), 6)

    def test_edge_case_single_element_list_with_single_element_sublist_with_single_element_subsublist(self):
        test_list = [[1], [2, 3], [4, 5, 6]]
        self.assertEqual(cummulative_sum(test_list), 21)

    def test_edge_case_single_element_list_with_single_element_sublist_with_single_element_subsublist_with_single_element_subsubsublist(self):
        test_list = [[1], [2, 3, 4], [5, 6, 7, 8]]
        self.assertEqual(cummulative_sum(test_list), 36)

    def test_edge_case_single_element_list_with_single_element_sublist_with_single_element_subsublist_with_single_element_subsubsublist_with_single_element_subsubsubsublist(self):
        test_list = [[1], [2, 3, 4, 5], [6, 7, 8, 9, 10]]
        self.assertEqual(cummulative_sum(test_list), 55)

    def test_edge_case_single_element_list_with_single_element_sublist_with_single_element_subsublist_with_single_element_subsubsublist_with_single_element_subsubsubsublist_with_single_element_subsubsubsubsublist(self):
        test_list = [[1], [2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]
        self.assertEqual(cummulative_sum(test_list), 78)

    def test_edge_case_single_element_list_with_single_element_sublist_with_single_element_subsublist_with_single_element_subsubsublist_with_single_element_subsubsubsublist_with_single_element_subsubsubsubsublist_with_single_element_subsubsubsubsubsublist(self):
        test_list = [[1], [2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]]
        self.assertEqual(cummulative_sum(test_list), 105)

    def test_edge_case_single_element_list_with_single_element_sublist_with_single_element_subsublist_with_single_element_subsubsublist_with_single_element_subsubsubsublist_with_single_element_subsubsubsubsublist_with_single_element_subsubsubsubsubsublist_with_single_element_subsubsubsubsubsubsublist(self):
        test_list = [[1], [2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16]]
        self.assertEqual(cummulative_sum(test_list), 144)

    def test_edge_case_single_element_list_with_single_element_sublist_with_single_element_subsublist_with_single_element_subsubsublist_with_single_element_subsubsubsublist_with_single_element_subsubsubsubsublist_with_single_element_subsubsubsubsubsublist_with_single_element_subsubsubsubsubsubsublist_with_single_element_subsubsubsubsubsubsubsublist(self):
        test_list = [[1], [2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18]]
        self.assertEqual(cummulative_sum(test_list), 204)

    def test_edge_case_single_element_list_with_single_element_sublist_with_single_element_subsublist_with_single_element_subsubsublist_with_single_element_subsubsubsublist_with_single_element_subsubsubsubsublist_with_single_element_subsubsubsubsubsublist_with_single_element_subsubsubsubsubsubsublist_with_single_element_subsubsubsubsubsubsubsublist_with_single_element_subsubsubsubsubsubsubsubsublist(self):
        test_list = [[1], [2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17,