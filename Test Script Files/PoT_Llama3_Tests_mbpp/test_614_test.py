import unittest
from mbpp_614_code import cummulative_sum

class TestCummulativeSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(cummulative_sum([[1, 2], [3, 4], [5, 6]]), 21)

    def test_edge_case_empty_list(self):
        self.assertEqual(cummulative_sum([]), 0)

    def test_edge_case_single_element_list(self):
        self.assertEqual(cummulative_sum([[1, 2, 3]]), 6)

    def test_edge_case_single_element_sublist(self):
        self.assertEqual(cummulative_sum([[1], [2]]), 3)

    def test_edge_case_all_sublists_empty(self):
        self.assertEqual(cummulative_sum([[], [], []]), 0)

    def test_edge_case_all_sublists_single_element(self):
        self.assertEqual(cummulative_sum([[1], [2], [3]]), 6)

    def test_edge_case_all_sublists_single_element_sublist(self):
        self.assertEqual(cummulative_sum([[1], [2], [3]]), 6)

    def test_edge_case_all_sublists_sublists_of_sublists(self):
        self.assertEqual(cummulative_sum([[1, 2], [3, 4], [5, 6]]), 21)

    def test_edge_case_all_sublists_sublists_of_sublists_of_sublists(self):
        self.assertEqual(cummulative_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 45)
