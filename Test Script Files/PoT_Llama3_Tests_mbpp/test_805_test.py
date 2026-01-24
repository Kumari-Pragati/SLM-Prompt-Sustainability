import unittest
from mbpp_805_code import max_sum_list

class TestMaxSumList(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_sum_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [9, 8, 7])

    def test_edge_case_empty_list(self):
        self.assertEqual(max_sum_list([]), [])

    def test_edge_case_single_list(self):
        self.assertEqual(max_sum_list([[1, 2, 3]]), [[1, 2, 3]])

    def test_edge_case_single_element_list(self):
        self.assertEqual(max_sum_list([[1]]), [[1]])

    def test_edge_case_single_element_list_with_negative_numbers(self):
        self.assertEqual(max_sum_list([[-1]]), [[-1]])

    def test_edge_case_single_element_list_with_zero(self):
        self.assertEqual(max_sum_list([[0]]), [[0]])

    def test_edge_case_single_element_list_with_positive_numbers(self):
        self.assertEqual(max_sum_list([[1]]), [[1]])

    def test_edge_case_multiple_lists(self):
        self.assertEqual(max_sum_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [9, 8, 7])

    def test_edge_case_multiple_lists_with_negative_numbers(self):
        self.assertEqual(max_sum_list([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), [-1, -2, -3])

    def test_edge_case_multiple_lists_with_zero(self):
        self.assertEqual(max_sum_list([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), [0, 0, 0])

    def test_edge_case_multiple_lists_with_positive_numbers(self):
        self.assertEqual(max_sum_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [9, 8, 7])
