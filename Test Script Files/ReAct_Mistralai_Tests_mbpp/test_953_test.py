import unittest
from mbpp_953_code import subset

class TestSubset(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(subset([], 0), 0)

    def test_single_element(self):
        self.assertEqual(subset([1], 1), 1)

    def test_duplicate_elements(self):
        self.assertEqual(subset([1, 1, 2], 2), 2)
        self.assertEqual(subset([1, 1, 1, 2], 3), 1)

    def test_sorted_array(self):
        self.assertEqual(subset([1, 2, 2, 3, 3, 4], 6), 1)
        self.assertEqual(subset([1, 1, 2, 2, 3, 3, 4], 7), 1)

    def test_unsorted_array(self):
        self.assertEqual(subset([4, 3, 3, 2, 2, 1], 6), 1)
        self.assertEqual(subset([4, 3, 3, 2, 2, 1], 7), 1)

    def test_negative_n(self):
        with self.assertRaises(ValueError):
            subset([1, 2, 3], -1)

    def test_zero_n(self):
        self.assertEqual(subset([1, 2, 3], 0), 0)

    def test_n_larger_than_len(self):
        with self.assertRaises(IndexError):
            subset([1, 2, 3], len([1, 2, 3]) + 1)
