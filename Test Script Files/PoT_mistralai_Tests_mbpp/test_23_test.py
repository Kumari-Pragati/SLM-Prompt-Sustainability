import unittest
from mbpp_23_code import maximum_Sum

class TestMaximumSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 27)
        self.assertEqual(maximum_Sum([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), 21)
        self.assertEqual(maximum_Sum([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 0)

    def test_edge_case_empty_list(self):
        self.assertEqual(maximum_Sum([]), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(maximum_Sum([[1]]), 1)
        self.assertEqual(maximum_Sum([[-1]]), -1)

    def test_edge_case_single_element_list(self):
        self.assertEqual(maximum_Sum([[1], [2], [3]]), 3)
        self.assertEqual(maximum_Sum([[-1], [-2], [-3]]), -3)

    def test_corner_case_negative_numbers(self):
        self.assertEqual(maximum_Sum([[-1, 2, -3], [4, -5, 6], [-7, 8, -9]]), 15)
