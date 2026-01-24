import unittest
from mbpp_728_code import sum_list

class TestSumList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_list([1, 2, 3], [4, 5, 6]), [5, 7, 9])

    def test_edge_case_empty_list(self):
        self.assertEqual(sum_list([], []), [])

    def test_edge_case_single_element(self):
        self.assertEqual(sum_list([1], [2]), [3])

    def test_edge_case_single_element_empty(self):
        self.assertEqual(sum_list([1], []), [])

    def test_edge_case_empty_list_single_element(self):
        self.assertEqual(sum_list([], [1]), [])

    def test_edge_case_equal_length_lists(self):
        self.assertEqual(sum_list([1, 2, 3], [4, 5, 6]), [5, 7, 9])

    def test_edge_case_unequal_length_lists(self):
        self.assertEqual(sum_list([1, 2, 3], [4, 5]), [5, 7, 3])

    def test_edge_case_negative_numbers(self):
        self.assertEqual(sum_list([-1, 2, 3], [4, -5, 6]), [3, -3, 9])

    def test_edge_case_zero(self):
        self.assertEqual(sum_list([0, 0], [0, 0]), [0, 0])

    def test_edge_case_negative_and_positive(self):
        self.assertEqual(sum_list([-1, 2, 3], [4, -5, 6]), [3, -3, 9])
