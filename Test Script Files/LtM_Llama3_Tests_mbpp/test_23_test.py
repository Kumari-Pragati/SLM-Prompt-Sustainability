import unittest
from mbpp_23_code import maximum_Sum

class TestMaximumSum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6]]), 14)

    def test_empty_input(self):
        self.assertEqual(maximum_Sum([]), -100000)

    def test_single_element(self):
        self.assertEqual(maximum_Sum([[1]]), 1)

    def test_negative_numbers(self):
        self.assertEqual(maximum_Sum([[-1, 2, 3], [4, 5, 6]]), 14)

    def test_max_value(self):
        self.assertEqual(maximum_Sum([[100, 200, 300]]), 600)

    def test_min_value(self):
        self.assertEqual(maximum_Sum([[-100, -50, 0]]), 0)

    def test_multiple_max_values(self):
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 14)
