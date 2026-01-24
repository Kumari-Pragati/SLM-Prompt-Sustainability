import unittest
from mbpp_144_code import sum_Pairs

class TestSumPairs(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(sum_Pairs([], 0), 0)

    def test_single_element_array(self):
        for num in range(10):
            self.assertEqual(sum_Pairs([num], 1), 0)

    def test_positive_array(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(sum_Pairs(arr, len(arr)), 15)

    def test_negative_array(self):
        arr = [-1, -2, -3, -4, -5]
        self.assertEqual(sum_Pairs(arr, len(arr)), -15)

    def test_zero_array(self):
        self.assertEqual(sum_Pairs([0], 1), 0)
        self.assertEqual(sum_Pairs([0, 0], 2), 0)

    def test_negative_n(self):
        self.assertRaises(ValueError, lambda: sum_Pairs([1, 2, 3], -1))
        self.assertRaises(ValueError, lambda: sum_Pairs([], -1))
        self.assertRaises(ValueError, lambda: sum_Pairs([1], -1))

    def test_out_of_range_index(self):
        arr = [1, 2, 3, 4, 5]
        self.assertRaises(IndexError, lambda: sum_Pairs, arr, len(arr)+1)
