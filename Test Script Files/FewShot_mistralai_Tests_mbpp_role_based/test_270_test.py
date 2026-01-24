import unittest
from mbpp_270_code import sum_even_and_even_index

class TestSumEvenAndEvenIndex(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_even_and_even_index([], 0), 0)

    def test_single_even_element(self):
        self.assertEqual(sum_even_and_even_index([2], 1), 2)

    def test_single_odd_element(self):
        self.assertEqual(sum_even_and_even_index([1], 1), 0)

    def test_all_even_elements(self):
        self.assertEqual(sum_even_and_even_index([2, 4, 6], 3), 12)

    def test_all_odd_elements(self):
        self.assertEqual(sum_even_and_even_index([1, 3, 5], 3), 0)

    def test_mixed_elements(self):
        self.assertEqual(sum_even_and_even_index([1, 2, 3, 4, 5, 6], 6), 12)

    def test_negative_elements(self):
        self.assertEqual(sum_even_and_even_index([-2, -4, -6], 3), -12)

    def test_index_out_of_range(self):
        self.assertRaises(IndexError, lambda: sum_even_and_even_index([1, 2, 3], 4))

    def test_negative_index(self):
        self.assertRaises(IndexError, lambda: sum_even_and_even_index([1, 2, 3], -1))
