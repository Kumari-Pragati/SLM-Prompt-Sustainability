import unittest
from mbpp_633_code import pair_OR_Sum

class TestPairORSum(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(pair_OR_Sum([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(pair_OR_Sum([1], 1), 0)

    def test_two_elements_array(self):
        self.assertEqual(pair_OR_Sum([1, 2], 2), 1)

    def test_three_elements_array(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3], 3), 2)

    def test_four_elements_array(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4], 4), 2)

    def test_five_elements_array(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4, 5], 5), 4)

    def test_six_elements_array(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4, 5, 6], 6), 4)

    def test_large_array(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 8)

    def test_negative_elements_array(self):
        self.assertEqual(pair_OR_Sum([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10], 10), 8)

    def test_mixed_elements_array(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10], 20), 8)
