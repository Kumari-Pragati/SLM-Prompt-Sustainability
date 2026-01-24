import unittest
from mbpp_270_code import sum_even_and_even_index

class TestSumEvenAndEvenIndex(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_even_and_even_index([], 0), 0)

    def test_all_odd_numbers(self):
        self.assertEqual(sum_even_and_even_index([1, 3, 5, 7], 4), 0)

    def test_all_even_numbers(self):
        self.assertEqual(sum_even_and_even_index([2, 4, 6, 8], 4), 20)

    def test_mixed_numbers(self):
        self.assertEqual(sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8], 8), 20)

    def test_negative_numbers(self):
        self.assertEqual(sum_even_and_even_index([-2, -4, -6, -8], 4), 0)

    def test_negative_and_positive_numbers(self):
        self.assertEqual(sum_even_and_even_index([-2, -4, 2, 4, -6, 6], 6), 8)

    def test_single_number(self):
        self.assertEqual(sum_even_and_even_index([2], 1), 2)

    def test_out_of_range_index(self):
        self.assertRaises(IndexError, lambda: sum_even_and_even_index([1, 2, 3], 4))

    def test_negative_index(self):
        self.assertRaises(IndexError, lambda: sum_even_and_even_index([1, 2, 3], -1))
