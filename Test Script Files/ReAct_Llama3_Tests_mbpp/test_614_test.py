import unittest
from mbpp_614_code import cummulative_sum

class TestCummulativeSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(cummulative_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 36)

    def test_edge_case_empty_list(self):
        self.assertEqual(cummulative_sum([]), 0)

    def test_edge_case_single_element_list(self):
        self.assertEqual(cummulative_sum([[1, 2, 3]]), 6)

    def test_edge_case_single_element_sublist(self):
        self.assertEqual(cummulative_sum([[1], [2], [3]]), 6)

    def test_edge_case_single_element_sublist_with_zero(self):
        self.assertEqual(cummulative_sum([[0], [0], [0]]), 0)

    def test_edge_case_single_element_sublist_with_negative(self):
        self.assertEqual(cummulative_sum([[1], [2], [-3]]), 0)

    def test_edge_case_single_element_sublist_with_negative_and_positive(self):
        self.assertEqual(cummulative_sum([[1], [2], [-3]]), 0)

    def test_edge_case_single_element_sublist_with_negative_and_positive_and_zero(self):
        self.assertEqual(cummulative_sum([[1], [2], [0]]), 3)

    def test_edge_case_single_element_sublist_with_negative_and_positive_and_zero_and_negative(self):
        self.assertEqual(cummulative_sum([[1], [2], [0, -3]]), 0)

    def test_edge_case_single_element_sublist_with_negative_and_positive_and_zero_and_negative_and_positive(self):
        self.assertEqual(cummulative_sum([[1], [2], [0, -3, 4]]), 3)

    def test_edge_case_single_element_sublist_with_negative_and_positive_and_zero_and_negative_and_positive_and_negative(self):
        self.assertEqual(cummulative_sum([[1], [2], [0, -3, 4, -5]]), 0)
