import unittest
from mbpp_270_code import sum_even_and_even_index

class TestSumEvenAndEvenIndex(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_even_and_even_index([], 0), 0)

    def test_single_even_element(self):
        self.assertEqual(sum_even_and_even_index([2], 1), 2)

    def test_single_odd_element(self):
        self.assertEqual(sum_even_and_even_index([1], 1), 0)

    def test_multiple_even_elements(self):
        self.assertEqual(sum_even_and_even_index([2, 4, 6], 3), 12)

    def test_multiple_odd_elements(self):
        self.assertEqual(sum_even_and_even_index([1, 3, 5], 3), 0)

    def test_mixed_elements(self):
        self.assertEqual(sum_even_and_even_index([1, 2, 3, 4, 5, 6], 6), 12)

    def test_negative_numbers(self):
        self.assertEqual(sum_even_and_even_index([-2, -4, -6], 3), -12)

    def test_out_of_range_index(self):
        with self.assertRaises(IndexError):
            sum_even_and_even_index([1, 2, 3], 4)

    def test_negative_index(self):
        with self.assertRaises(IndexError):
            sum_even_and_even_index([1, 2, 3], -1)
