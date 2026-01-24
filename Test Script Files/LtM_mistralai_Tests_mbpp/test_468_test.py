import unittest
from mbpp_468_code import max_product

class TestMaxProduct(unittest.TestCase):

    def test_simple_positive(self):
        self.assertEqual(max_product([1, 2, 3, 4], 4), 24)

    def test_simple_negative(self):
        self.assertEqual(max_product([-1, -2, -3, -4], 4), -24)

    def test_single_element(self):
        self.assertEqual(max_product([5], 1), 5)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            max_product([], 0)

    def test_negative_n(self):
        with self.assertRaises(ValueError):
            max_product([1, 2, 3], -1)

    def test_zero_element(self):
        self.assertEqual(max_product([0], 1), 0)

    def test_duplicates(self):
        self.assertEqual(max_product([1, 1, 2, 3], 4), 6)

    def test_decreasing_sequence(self):
        self.assertEqual(max_product([5, 4, 3, 2, 1], 5), 120)

    def test_increasing_sequence(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5], 5), 120)

    def test_alternating_sequence(self):
        self.assertEqual(max_product([1, -1, 1, -1, 1], 5), 1)
