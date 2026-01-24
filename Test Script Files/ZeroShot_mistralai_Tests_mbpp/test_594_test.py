import unittest
from mbpp_594_code import diff_even_odd

class TestDiffEvenOdd(unittest.TestCase):

    def test_empty_list(self):
        self.assertAlmostEqual(diff_even_odd([]), 0)

    def test_all_even_list(self):
        self.assertAlmostEqual(diff_even_odd([2, 4, 6]), 0)

    def test_all_odd_list(self):
        self.assertAlmostEqual(diff_even_odd([1, 3, 5]), 0)

    def test_mixed_list(self):
        self.assertAlmostEqual(diff_even_odd([1, 2, 3, 4, 5]), 1)
        self.assertAlmostEqual(diff_even_odd([1, 2, 3, 4, 5, 6]), 2)
        self.assertAlmostEqual(diff_even_odd([1, 2, 3, 4, 5, 6, 7]), 3)

    def test_single_even_list(self):
        self.assertAlmostEqual(diff_even_odd([2]), 0)

    def test_single_odd_list(self):
        self.assertAlmostEqual(diff_even_odd([1]), 0)

    def test_negative_numbers(self):
        self.assertAlmostEqual(diff_even_odd([-1, -2, -3]), 1)
        self.assertAlmostEqual(diff_even_odd([-1, -2, -3, -4]), 2)
