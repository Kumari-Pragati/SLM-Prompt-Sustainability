import unittest
from mbpp_23_code import maximum_Sum

class TestMaximumSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 24)

    def test_single_element(self):
        self.assertEqual(maximum_Sum([[5]]), 5)

    def test_empty_list(self):
        self.assertEqual(maximum_Sum([]), -100000)

    def test_negative_numbers(self):
        self.assertEqual(maximum_Sum([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), -6)

    def test_mixed_numbers(self):
        self.assertEqual(maximum_Sum([[1, -2, 3], [-4, 5, -6], [7, -8, 9]]), 24)

    def test_zero_sum(self):
        self.assertEqual(maximum_Sum([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 0)

    def test_empty_sublists(self):
        self.assertEqual(maximum_Sum([[], [], []]), -100000)

    def test_single_sublist(self):
        self.assertEqual(maximum_Sum([[1, 2, 3]]), 6)

    def test_large_numbers(self):
        self.assertEqual(maximum_Sum([[100000, 200000, 300000], [400000, 500000, 600000], [700000, 800000, 900000]]), 2400000)
