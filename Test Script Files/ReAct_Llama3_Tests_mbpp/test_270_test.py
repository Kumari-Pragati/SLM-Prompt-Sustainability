import unittest
from mbpp_270_code import sum_even_and_even_index

class TestSumEvenAndEvenIndex(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(sum_even_and_even_index([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(sum_even_and_even_index([2], 1), 2)

    def test_multiple_even_elements(self):
        self.assertEqual(sum_even_and_even_index([2, 4, 6, 8], 4), 20)

    def test_multiple_elements_with_mixed_even_odd(self):
        self.assertEqual(sum_even_and_even_index([1, 2, 3, 4, 5, 6], 6), 12)

    def test_array_length_less_than_index(self):
        self.assertEqual(sum_even_and_and_index([1, 2, 3, 4, 5, 6], 3), 0)

    def test_array_length_equal_to_index(self):
        self.assertEqual(sum_even_and_even_index([1, 2, 3, 4, 5, 6], 6), 12)

    def test_array_length_greater_than_index(self):
        self.assertEqual(sum_even_and_even_index([1, 2, 3, 4, 5, 6], 10), 12)
