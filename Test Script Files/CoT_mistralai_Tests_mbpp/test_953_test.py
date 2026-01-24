import unittest
from mbpp_953_code import subset

class TestSubset(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(subset([], 0), 0)

    def test_single_element(self):
        self.assertEqual(subset([1], 1), 1)

    def test_duplicates(self):
        self.assertEqual(subset([1, 1, 2], 2), 2)
        self.assertEqual(subset([1, 1, 1, 2], 3), 3)
        self.assertEqual(subset([1, 1, 1, 1, 2], 4), 4)

    def test_sorted_list(self):
        self.assertEqual(subset([1, 2, 2, 3, 3], 4), 2)
        self.assertEqual(subset([1, 1, 2, 2, 3, 3], 5), 2)

    def test_unsorted_list(self):
        self.assertEqual(subset([3, 2, 2, 1], 3), 2)
        self.assertEqual(subset([3, 2, 2, 1, 1], 4), 3)

    def test_negative_n(self):
        with self.assertRaises(ValueError):
            subset([1, 2, 3], -1)

    def test_empty_n(self):
        with self.assertRaises(ValueError):
            subset([1, 2, 3], 0)

    def test_non_iterable_ar(self):
        with self.assertRaises(TypeError):
            subset(123, 4)
