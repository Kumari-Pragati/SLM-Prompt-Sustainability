import unittest
from mbpp_23_code import maximum_Sum

class TestMaximumSum(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 36)

    def test_negative_numbers(self):
        self.assertEqual(maximum_Sum([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), -6)

    def test_mixed_numbers(self):
        self.assertEqual(maximum_Sum([[1, -2, 3], [-4, 5, -6], [7, -8, 9]]), 15)

    def test_empty_list(self):
        self.assertEqual(maximum_Sum([]), -100000)

    def test_single_list(self):
        self.assertEqual(maximum_Sum([[1, 2, 3]]), 6)

    def test_single_number(self):
        self.assertEqual(maximum_Sum([[1]]), 1)
