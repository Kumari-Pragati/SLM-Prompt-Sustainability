import unittest
from mbpp_144_code import sum_Pairs

class TestSumPairs(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(sum_Pairs([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(sum_Pairs([1], 1), 0)

    def test_two_element_array(self):
        self.assertEqual(sum_Pairs([1, 2], 2), 0)

    def test_three_element_array(self):
        self.assertEqual(sum_Pairs([1, 2, 3], 3), 0)

    def test_four_element_array(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4], 4), 0)

    def test_five_element_array(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4, 5], 5), 0)

    def test_edge_case_n_is_one(self):
        self.assertEqual(sum_Pairs([1, 2], 1), 1)

    def test_edge_case_n_is_array_length(self):
        self.assertEqual(sum_Pairs([1, 2, 3], 3), 0)

    def test_edge_case_n_is_zero(self):
        with self.assertRaises(IndexError):
            sum_Pairs([1, 2, 3], 0)

    def test_edge_case_n_is_negative(self):
        with self.assertRaises(IndexError):
            sum_Pairs([1, 2, 3], -1)
