import unittest
from mbpp_594_code import diff_even_odd

class TestDiffEvenOdd(unittest.TestCase):
    def test_empty_list(self):
        self.assertAlmostEqual(diff_even_odd([]), 0)

    def test_single_even_number(self):
        self.assertAlmostEqual(diff_even_odd([2]), 2)

    def test_single_odd_number(self):
        self.assertAlmostEqual(diff_even_odd([1]), -1)

    def test_mixed_list(self):
        self.assertAlmostEqual(diff_even_odd([1, 2, 3, 4, 5]), 2)

    def test_repeated_even_numbers(self):
        self.assertAlmostEqual(diff_even_odd([2, 2, 2, 1]), 2)

    def test_repeated_odd_numbers(self):
        self.assertAlmostEqual(diff_even_odd([1, 1, 1, 2]), -2)

    def test_list_with_zero(self):
        self.assertAlmostEqual(diff_even_odd([0, 1, 2, 3, 4]), 1)

    def test_list_with_negative_numbers(self):
        self.assertAlmostEqual(diff_even_odd([-1, -2, -3, -4]), 1)
