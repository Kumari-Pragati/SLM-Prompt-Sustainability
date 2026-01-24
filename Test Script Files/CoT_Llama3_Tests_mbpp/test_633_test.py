import unittest
from mbpp_633_code import pair_OR_Sum

class TestPairORSum(unittest.TestCase):

    def test_pair_OR_Sum_empty_array(self):
        self.assertEqual(pair_OR_Sum([], 0), 0)

    def test_pair_OR_Sum_single_element_array(self):
        self.assertEqual(pair_OR_Sum([1], 1), 1)

    def test_pair_OR_Sum_two_elements_array(self):
        self.assertEqual(pair_OR_Sum([1, 2], 2), 1)

    def test_pair_OR_Sum_three_elements_array(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3], 3), 2)

    def test_pair_OR_Sum_four_elements_array(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4], 4), 2)

    def test_pair_OR_Sum_five_elements_array(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4, 5], 5), 2)

    def test_pair_OR_Sum_negative_elements_array(self):
        self.assertEqual(pair_OR_Sum([-1, -2, -3], 3), -1)

    def test_pair_OR_Sum_mixed_elements_array(self):
        self.assertEqual(pair_OR_Sum([1, 2, -3, 4], 4), 1)

    def test_pair_OR_Sum_duplicates_elements_array(self):
        self.assertEqual(pair_OR_Sum([1, 1, 2, 2], 4, ), 0)
