import unittest
from mbpp_614_code import cummulative_sum

class TestCummulativeSum(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(cummulative_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 45)

    def test_edge_case_empty_list(self):
        self.assertEqual(cummulative_sum([]), 0)

    def test_edge_case_single_element_list(self):
        self.assertEqual(cummulative_sum([[1, 2, 3]]), 6)

    def test_edge_case_single_element_sublist(self):
        self.assertEqual(cummulative_sum([[1], [2], [3]]), 6)

    def test_edge_case_single_element_sublist_with_zero(self):
        self.assertEqual(cummulative_sum([[0], [0], [0]]), 0)

    def test_edge_case_single_element_sublist_with_negative(self):
        self.assertEqual(cummulative_sum([[-1], [0], [1]]), 0)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            cummulative_sum("Invalid input")

    def test_invalid_input_non_list_of_lists(self):
        with self.assertRaises(TypeError):
            cummulative_sum([1, 2, 3])
