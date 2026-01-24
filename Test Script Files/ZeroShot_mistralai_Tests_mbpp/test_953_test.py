import unittest
from mbpp_953_code import subset

class TestSubset(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(subset([], 0), 0)

    def test_single_element(self):
        self.assertEqual(subset([1], 1), 1)

    def test_duplicate_elements(self):
        self.assertEqual(subset([1, 1, 1], 3), 1)

    def test_unique_elements(self):
        self.assertEqual(subset([1, 2, 3], 3), 3)

    def test_longer_list(self):
        self.assertEqual(subset([1, 2, 2, 3, 4, 4, 5], 7), 2)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            subset([1, 2, 3], -1)

    def test_zero_input(self):
        with self.assertRaises(ValueError):
            subset([], 0)
