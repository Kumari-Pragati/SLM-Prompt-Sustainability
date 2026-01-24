import unittest
from mbpp_881_code import sum_even_odd

class TestSumEvenOdd(unittest.TestCase):

    def test_sum_even_odd_with_all_even(self):
        self.assertEqual(sum_even_odd([2, 4, 6]), 8)

    def test_sum_even_odd_with_all_odd(self):
        self.assertEqual(sum_even_odd([1, 3, 5]), 6)

    def test_sum_even_odd_with_mixed(self):
        self.assertEqual(sum_even_odd([1, 2, 3, 4, 5, 6]), 4)

    def test_sum_even_odd_with_negative_numbers(self):
        self.assertEqual(sum_even_odd([-1, -2, -3, -4, -5, -6]), -4)

    def test_sum_even_odd_with_zero(self):
        self.assertEqual(sum_even_odd([0, 1, 2, 3, 4, 5]), 1)

    def test_sum_even_odd_with_empty_list(self):
        self.assertEqual(sum_even_odd([]), -1)
