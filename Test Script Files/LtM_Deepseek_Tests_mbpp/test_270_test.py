import unittest
from mbpp_270_code import sum_even_and_even_index

class TestSumEvenAndEvenIndex(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(sum_even_and_even_index([2, 4, 6, 8], 4), 20)

    def test_edge_conditions(self):
        self.assertEqual(sum_even_and_even_index([], 0), 0)
        self.assertEqual(sum_even_and_even_index([1, 3, 5, 7], 4), 0)
        self.assertEqual(sum_even_and_even_index([2, 3, 4, 5], 4), 6)

    def test_complex_cases(self):
        self.assertEqual(sum_even_and_even_index([10, 20, 30, 40], 4), 60)
        self.assertEqual(sum_even_and_even_index([2, 4, 6, 8, 10, 12], 6), 30)
