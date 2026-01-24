import unittest
from mbpp_953_code import subset

class TestSubset(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(subset([1, 2, 2, 3, 3, 3], 6), 3)

    def test_single_element(self):
        self.assertEqual(subset([1], 1), 1)

    def test_empty_list(self):
        self.assertEqual(subset([], 0), 0)

    def test_repeated_elements(self):
        self.assertEqual(subset([1, 1, 1, 1], 4), 4)

    def test_sorted_list(self):
        self.assertEqual(subset([1, 2, 2, 3, 3, 3], 6), 3)

    def test_unsorted_list(self):
        self.assertEqual(subset([3, 3, 3, 2, 2, 1], 6), 3)

    def test_negative_numbers(self):
        self.assertEqual(subset([-1, -1, -1, 1, 1, 1], 6), 3)

    def test_large_numbers(self):
        self.assertEqual(subset([1000, 1000, 1000, 2000, 2000], 5), 3)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            subset("1, 2, 2, 3, 3, 3", 6)
