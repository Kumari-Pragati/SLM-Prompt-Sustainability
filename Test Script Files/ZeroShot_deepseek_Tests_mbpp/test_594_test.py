import unittest
from mbpp_594_code import diff_even_odd

class TestDiffEvenOdd(unittest.TestCase):

    def test_diff_even_odd_with_all_even(self):
        self.assertEqual(diff_even_odd([2, 4, 6]), 0)

    def test_diff_even_odd_with_all_odd(self):
        self.assertEqual(diff_even_odd([1, 3, 5]), 4)

    def test_diff_even_odd_with_mixed(self):
        self.assertEqual(diff_even_odd([1, 2, 3, 4, 5, 6]), 2)

    def test_diff_even_odd_with_negative_numbers(self):
        self.assertEqual(diff_even_odd([-1, -2, -3, -4, -5, -6]), -2)

    def test_diff_even_odd_with_zero(self):
        self.assertEqual(diff_even_odd([0, 1, 2, 3, 4, 5]), 0)

    def test_diff_even_odd_with_empty_list(self):
        self.assertEqual(diff_even_odd([]), -1)
