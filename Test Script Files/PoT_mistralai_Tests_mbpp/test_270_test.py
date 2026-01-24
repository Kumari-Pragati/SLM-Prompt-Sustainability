import unittest
from mbpp_270_code import sum_even_and_even_index

class TestSumEvenAndEvenIndex(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 12)
        self.assertEqual(sum_even_and_even_index([2, 4, 6, 8, 10], 5), 20)
        self.assertEqual(sum_even_and_even_index([0, 1, 2, 3, 4, 5, 6], 7), 12)

    def test_edge_case_empty_list(self):
        self.assertEqual(sum_even_and_even_index([], 0), 0)

    def test_edge_case_odd_length(self):
        self.assertEqual(sum_even_and_even_index([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(sum_even_and_even_index([0, 1, 2, 3, 4], 5), 0)

    def test_corner_case_all_even(self):
        self.assertEqual(sum_even_and_even_index([0, 2, 4, 6, 8], 5), 20)

    def test_corner_case_all_odd(self):
        self.assertEqual(sum_even_and_even_index([1, 3, 5, 7, 9], 5), 0)
