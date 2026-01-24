import unittest
from mbpp_195_code import first

class TestFirst(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(first([], 1, 0), -1)

    def test_single_element(self):
        self.assertEqual(first([1], 1, 0), 0)
        self.assertEqual(first([1], 2, 0), -1)
        self.assertEqual(first([1], 1, 1), 0)

    def test_ordered_list(self):
        self.assertEqual(first([1, 2, 3, 4, 5], 2, 5), 2)
        self.assertEqual(first([1, 2, 3, 4, 5], 6, 5), -1)
        self.assertEqual(first([1, 2, 3, 4, 5], 1, 0), -1)
        self.assertEqual(first([1, 2, 3, 4, 5], 5, 5), 4)

    def test_unordered_list(self):
        self.assertEqual(first([5, 3, 1, 4, 2], 2, 5), 2)
        self.assertEqual(first([5, 3, 1, 4, 2], 6, 5), -1)
        self.assertEqual(first([5, 3, 1, 4, 2], 1, 0), -1)
        self.assertEqual(first([5, 3, 1, 4, 2], 5, 5), 4)

    def test_negative_numbers(self):
        self.assertEqual(first([-1, -2, -3, -4, -5], -2, 5), 2)
        self.assertEqual(first([-1, -2, -3, -4, -5], -6, 5), -1)
        self.assertEqual(first([-1, -2, -3, -4, -5], -1, 0), -1)
        self.assertEqual(first([-1, -2, -3, -4, -5], -5, 5), 4)
