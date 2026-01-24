import unittest
from mbpp_23_code import maximum_Sum

class TestMaximumSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6]]), 9)

    def test_edge_case_empty_list(self):
        self.assertEqual(maximum_Sum([]), -100000)

    def test_edge_case_single_element_list(self):
        self.assertEqual(maximum_Sum([[1]]), 1)

    def test_edge_case_single_element_sublist(self):
        self.assertEqual(maximum_Sum([[1, 2, 3], [4]]), 4)

    def test_edge_case_max_sum_at_start(self):
        self.assertEqual(maximum_Sum([[10, 20, 30], [4, 5, 6]]), 30)

    def test_edge_case_max_sum_at_end(self):
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 10]]), 10)

    def test_edge_case_max_sum_at_middle(self):
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 9)

    def test_edge_case_max_sum_at_start_and_end(self):
        self.assertEqual(maximum_Sum([[10, 20, 30], [4, 5, 6], [7, 8, 9]]), 30)

    def test_edge_case_max_sum_at_start_and_middle(self):
        self.assertEqual(maximum_Sum([[10, 20, 30], [4, 5, 6], [7, 8, 9, 10]]), 30)

    def test_edge_case_max_sum_at_end_and_middle(self):
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]), 10)

    def test_edge_case_max_sum_at_start_and_middle_and_end(self):
        self.assertEqual(maximum_Sum([[10, 20, 30], [4, 5, 6], [7, 8, 9, 10, 20]]), 30)
