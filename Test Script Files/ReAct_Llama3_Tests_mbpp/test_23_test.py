import unittest
from mbpp_23_code import maximum_Sum

class TestMaximumSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 18)

    def test_edge_case(self):
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6]]), 9)

    def test_empty_list(self):
        self.assertEqual(maximum_Sum([]), -100000)

    def test_single_element_list(self):
        self.assertEqual(maximum_Sum([[1, 2, 3]]), 6)

    def test_single_element_sublist(self):
        self.assertEqual(maximum_Sum([[1, 2, 3], [4]]), 6)

    def test_negative_numbers(self):
        self.assertEqual(maximum_Sum([[-1, -2, -3], [4, 5, 6]]), 9)

    def test_zero_sum(self):
        self.assertEqual(maximum_Sum([[0, 0, 0], [4, 5, 6]]), 9)
