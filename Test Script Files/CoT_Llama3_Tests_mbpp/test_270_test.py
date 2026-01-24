import unittest
from mbpp_270_code import sum_even_and_even_index

class TestSumEvenAndEvenIndex(unittest.TestCase):

    def test_sum_even_and_even_index_empty_array(self):
        self.assertEqual(sum_even_and_even_index([], 0), 0)

    def test_sum_even_and_even_index_single_element(self):
        self.assertEqual(sum_even_and_even_index([1], 1), 0)

    def test_sum_even_and_even_index_even_elements(self):
        self.assertEqual(sum_even_and_even_index([2, 4, 6, 8], 4), 20)

    def test_sum_even_and_even_index_odd_elements(self):
        self.assertEqual(sum_even_and_even_index([1, 3, 5, 7], 4, 0), 0)

    def test_sum_even_and_even_index_mixed_elements(self):
        self.assertEqual(sum_even_and_even_index([1, 2, 3, 4, 5, 6], 6), 12)

    def test_sum_even_and_even_index_negative_elements(self):
        self.assertEqual(sum_even_and_even_index([-2, -4, -6, -8], 4), -20)

    def test_sum_even_and_even_index_zero_elements(self):
        self.assertEqual(sum_even_and_even_index([0, 0, 0, 0], 4), 0)
