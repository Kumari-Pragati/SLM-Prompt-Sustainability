import unittest
from mbpp_633_code import pair_OR_Sum

class TestPairORSum(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(pair_OR_Sum([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(pair_OR_Sum([1], 1), 0)

    def test_two_element_array(self):
        self.assertEqual(pair_OR_Sum([1, 2], 2), 1)

    def test_three_element_array(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3], 3), 2)

    def test_four_element_array(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4], 4), 2)

    def test_five_element_array(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4, 5], 5), 2)

    def test_negative_numbers(self):
        self.assertEqual(pair_OR_Sum([-1, -2, -3, -4, -5], 5), -2)

    def test_positive_numbers(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4, 5], 5), 2)

    def test_mixed_numbers(self):
        self.assertEqual(pair_OR_Sum([-1, 1, -2, 2, -3, 3, -4, 4, -5, 5], 10), 0)
