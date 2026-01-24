import unittest
from mbpp_881_code import sum_even_odd

class TestSumEvenOdd(unittest.TestCase):
    def test_simple_even_and_odd(self):
        self.assertEqual(sum_even_odd([2, 3, 4, 5]), 2 + 5)
        self.assertEqual(sum_even_odd([-2, -3, 4, 5]), -2 + 5)
        self.assertEqual(sum_even_odd([2, -3, 4, -5]), 2 + -3)

    def test_single_even_or_odd(self):
        self.assertEqual(sum_even_odd([2]), 2)
        self.assertEqual(sum_even_odd([3]), 3)
        self.assertEqual(sum_even_odd([-2]), -2)
        self.assertEqual(sum_even_odd([-3]), -3)

    def test_empty_list(self):
        self.assertEqual(sum_even_odd([]), -1)

    def test_all_even(self):
        self.assertEqual(sum_even_odd([2, 4, 6]), 2 + 6)
        self.assertEqual(sum_even_odd([-2, -4, -6]), -2 + -6)

    def test_all_odd(self):
        self.assertEqual(sum_even_odd([1, 3, 5]), 1 + 3 + 5)
        self.assertEqual(sum_even_odd([-1, -3, -5]), -1 + -3 + -5)
