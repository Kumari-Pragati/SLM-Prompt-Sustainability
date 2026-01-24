import unittest
from mbpp_270_code import sum_even_and_even_index

class TestSumEvenAndEvenIndex(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(sum_even_and_even_index([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(sum_even_and_even_index([2], 1), 2)

    def test_even_indexed_elements(self):
        self.assertEqual(sum_even_and_even_index([2, 4, 6, 8], 4), 20)

    def test_odd_indexed_elements(self):
        self.assertEqual(sum_even_and_even_index([1, 3, 5, 7], 4), 0)

    def test_mixed_indexed_elements(self):
        self.assertEqual(sum_even_and_even_index([1, 2, 3, 4], 4), 6)

    def test_array_with_no_even_elements(self):
        self.assertEqual(sum_even_and_even_index([1, 3, 5, 7], 4), 0)

    def test_array_with_no_elements(self):
        self.assertEqual(sum_even_and_even_index([], 0), 0)

    def test_array_with_single_element(self):
        self.assertEqual(sum_even_and_even_index([5], 1), 0)

    def test_array_with_multiple_elements(self):
        self.assertEqual(sum_even_and_even_index([2, 4, 6, 8, 10], 5), 30)
