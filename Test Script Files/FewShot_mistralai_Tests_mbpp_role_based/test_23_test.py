import unittest
from mbpp_23_code import maximum_Sum

class TestMaximumSum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 24)

    def test_negative_numbers(self):
        self.assertEqual(maximum_Sum([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), 24)

    def test_empty_list(self):
        self.assertEqual(maximum_Sum([]), 0)

    def test_single_element_list(self):
        self.assertEqual(maximum_Sum([[1]]), 1)

    def test_zero_list(self):
        self.assertEqual(maximum_Sum([[0]]), 0)

    def test_mixed_numbers(self):
        self.assertEqual(maximum_Sum([[1, -2, 3], [-4, 5, 6], [7, -8, 9]]), 21)

    def test_negative_sum(self):
        self.assertEqual(maximum_Sum([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), -1)
