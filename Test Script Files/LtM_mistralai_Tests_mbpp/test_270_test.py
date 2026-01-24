import unittest
from mbpp_270_code import sum_even_and_even_index

class TestSumEvenAndEvenIndex(unittest.TestCase):

    def test_simple_even_array(self):
        self.assertEqual(sum_even_and_even_index([2, 4, 6], 3), 12)

    def test_simple_odd_array(self):
        self.assertEqual(sum_even_and_even_index([1, 3, 5], 3), 0)

    def test_empty_array(self):
        self.assertEqual(sum_even_and_even_index([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(sum_even_and_even_index([2], 1), 2)

    def test_single_even_element(self):
        self.assertEqual(sum_even_and_even_index([2], 0), 2)

    def test_single_odd_element(self):
        self.assertEqual(sum_even_and_even_index([1], 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(sum_even_and_even_index([-2, -4, -6], 3), 12)

    def test_large_numbers(self):
        self.assertEqual(sum_even_and_even_index([1000000, 1000002, 1000004], 3), 2000002)
