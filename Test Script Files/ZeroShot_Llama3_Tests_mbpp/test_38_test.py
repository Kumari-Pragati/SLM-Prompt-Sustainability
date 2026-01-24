import unittest
from mbpp_38_code import div_even_odd

class TestDivEvenOdd(unittest.TestCase):

    def test_division_by_zero(self):
        self.assertRaises(ZeroDivisionError, div_even_odd, [10, 20, 30, 40])

    def test_division_by_non_zero(self):
        self.assertAlmostEqual(div_even_odd([10, 20, 30, 40]), 0.5, places=5)

    def test_division_by_non_zero_with_negative_numbers(self):
        self.assertAlmostEqual(div_even_odd([-10, -20, -30, -40]), -0.5, places=5)

    def test_division_by_non_zero_with_mixed_numbers(self):
        self.assertAlmostEqual(div_even_odd([10, -20, 30, -40]), -0.5, places=5)

    def test_division_by_non_zero_with_no_evens(self):
        self.assertRaises(ZeroDivisionError, div_even_odd, [1, 3, 5, 7])

    def test_division_by_non_zero_with_no_odds(self):
        self.assertAlmostEqual(div_even_odd([10, 20, 30, 40]), 1.0, places=5)

    def test_division_by_non_zero_with_single_element(self):
        self.assertAlmostEqual(div_even_odd([10]), 1.0, places=5)

    def test_division_by_non_zero_with_empty_list(self):
        with self.assertRaises(IndexError):
            div_even_odd([])
