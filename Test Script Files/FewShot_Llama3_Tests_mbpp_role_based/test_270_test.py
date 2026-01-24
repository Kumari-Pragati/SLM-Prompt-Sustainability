import unittest
from mbpp_270_code import sum_even_and_even_index

class TestSumEvenAndEvenIndex(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(sum_even_and_even_index([], 5), 0)

    def test_single_element_array(self):
        self.assertEqual(sum_even_and_even_index([10], 1), 10)

    def test_multiple_even_elements(self):
        self.assertEqual(sum_even_and_even_index([2, 4, 6, 8], 4), 20)

    def test_multiple_odd_elements(self):
        self.assertEqual(sum_even_and_even_index([1, 3, 5, 7], 4), 0)

    def test_mixed_elements(self):
        self.assertEqual(sum_even_and_even_index([1, 2, 3, 4], 4), 6)

    def test_array_length_less_than_index(self):
        self.assertEqual(sum_even_and_even_index([1, 2, 3], 1), 0)

    def test_array_length_greater_than_index(self):
        self.assertEqual(sum_even_and_even_index([1, 2, 3, 4, 5, 6], 6), 12)
