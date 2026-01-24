import unittest
from mbpp_23_code import maximum_Sum

class TestMaximumSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(maximum_Sum([]), 0)

    def test_single_element_list(self):
        self.assertEqual(maximum_Sum([[1]]), 1)

    def test_positive_numbers(self):
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 24)

    def test_negative_numbers(self):
        self.assertEqual(maximum_Sum([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), -24)

    def test_mixed_numbers(self):
        self.assertEqual(maximum_Sum([[1, -2, 3], [-4, 5, 6], [7, -8, 9]]), 16)

    def test_list_with_zero(self):
        self.assertEqual(maximum_Sum([[0], [1], [2]]), 3)

    def test_list_with_only_zero(self):
        self.assertEqual(maximum_Sum([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 0)

    def test_list_with_only_negative_numbers(self):
        self.assertEqual(maximum_Sum([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), -24)

    def test_list_with_only_positive_numbers(self):
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 24)

    def test_list_with_empty_sublists(self):
        self.assertEqual(maximum_Sum([[1, 2, 3, ], [], [7, 8, 9]]), 15)

    def test_list_with_negative_and_positive_numbers(self):
        self.assertEqual(maximum_Sum([[1, -2, 3], [-4, 5, 6], [7, -8, 9]]), 16)

    def test_list_with_only_zero_and_empty_sublists(self):
        self.assertEqual(maximum_Sum([[0, 0, 0], [], [0, 0, 0]]), 0)
