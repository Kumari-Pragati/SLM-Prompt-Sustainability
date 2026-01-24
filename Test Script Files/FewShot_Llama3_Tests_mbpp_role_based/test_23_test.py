import unittest
from mbpp_23_code import maximum_Sum

class TestMaximumSum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6]]), 9)

    def test_edge_case_empty_list(self):
        self.assertEqual(maximum_Sum([]), -100000)

    def test_edge_case_single_element_list(self):
        self.assertEqual(maximum_Sum([[1, 2, 3]]), 6)

    def test_edge_case_single_element_sublist(self):
        self.assertEqual(maximum_Sum([[1, 2, 3], [1]]), 3)

    def test_edge_case_all_negative_numbers(self):
        self.assertEqual(maximum_Sum([[-1, -2, -3], [-4, -5, -6]]), -1)

    def test_edge_case_mixed_positive_and_negative_numbers(self):
        self.assertEqual(maximum_Sum([[1, 2, 3], [-4, -5, -6]]), 3)

    def test_edge_case_all_positive_numbers(self):
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6]]), 6)
