import unittest
from mbpp_564_code import count_Pairs

class TestCountPairs(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_Pairs([], 0), 0)

    def test_single_element(self):
        self.assertEqual(count_Pairs([1], 1), 0)

    def test_single_pair(self):
        self.assertEqual(count_Pairs([1, 2], 2), 1)

    def test_multiple_pairs(self):
        self.assertEqual(count_Pairs([1, 2, 3, 4, 5], 5), 5)

    def test_duplicate_elements(self):
        self.assertEqual(count_Pairs([1, 1, 2, 3, 4, 4, 5], 7), 3)

    def test_negative_numbers(self):
        self.assertEqual(count_Pairs([-1, -2, -3, -4, -5], 5), 5)

    def test_zero(self):
        self.assertEqual(count_Pairs([0], 1), 0)
        self.assertEqual(count_Pairs([0, 0], 2), 0)

    def test_large_numbers(self):
        self.assertEqual(count_Pairs([1000000, 1000001, 1000002], 3), 2)

    def test_out_of_bounds(self):
        with self.assertRaises(IndexError):
            count_Pairs([1, 2, 3], 0)
        with self.assertRaises(IndexError):
            count_Pairs([1, 2, 3], 4)
