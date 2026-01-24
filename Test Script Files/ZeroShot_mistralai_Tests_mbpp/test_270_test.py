import unittest
from mbpp_270_code import sum_even_and_even_index

class TestSumEvenAndEvenIndex(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_even_and_even_index([], 0), 0)

    def test_all_odd_numbers(self):
        self.assertEqual(sum_even_and_even_index([1, 3, 5, 7], 4), 0)

    def test_all_even_numbers(self):
        self.assertEqual(sum_even_and_even_index([2, 4, 6, 8], 4), 2 + 4)

    def test_mixed_numbers(self):
        self.assertEqual(sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8], 8), 2 + 4)

    def test_negative_numbers(self):
        self.assertEqual(sum_even_and_even_index([-2, -1, 0, 1, 2], 5), -2)

    def test_index_out_of_range(self):
        self.assertRaises(IndexError, lambda: sum_even_and_even_index([1, 2, 3], 4))
