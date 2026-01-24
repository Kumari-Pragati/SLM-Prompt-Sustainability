import unittest
from mbpp_594_code import diff_even_odd

class TestDiffEvenOdd(unittest.TestCase):
    def test_simple_even_and_odd(self):
        self.assertEqual(diff_even_odd([2, 3, 4, 5]), 1)
        self.assertEqual(diff_even_odd([0, 1, 2, 3]), 1)
        self.assertEqual(diff_even_odd([-2, -1, 0, 1]), 3)

    def test_single_even_or_odd(self):
        self.assertEqual(diff_even_odd([2]), 0)
        self.assertEqual(diff_even_odd([1]), 0)
        self.assertEqual(diff_even_odd([0]), 0)

    def test_empty_list(self):
        self.assertEqual(diff_even_odd([]), -1)

    def test_all_even(self):
        self.assertEqual(diff_even_odd([2, 4, 6]), 0)
        self.assertEqual(diff_even_odd([-2, -4, -6]), 0)

    def test_all_odd(self):
        self.assertEqual(diff_even_odd([1, 3, 5]), 0)
        self.assertEqual(diff_even_odd([-1, -3, -5]), 0)

    def test_min_max_values(self):
        self.assertEqual(diff_even_odd([-2147483648, -1, 0, 1, 2147483647]), 4294967295)
        self.assertEqual(diff_even_odd([-2147483647, -1, 0, 1, 2147483647]), -4294967295)
