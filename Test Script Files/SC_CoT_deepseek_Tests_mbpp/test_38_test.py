import unittest
from mbpp_38_code import div_even_odd

class TestDivEvenOdd(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(div_even_odd([1, 2, 3, 4, 5]), 0.6666666666666666)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            div_even_odd([])

    def test_all_odd_numbers(self):
        with self.assertRaises(ValueError):
            div_even_odd([1, 3, 5, 7, 9])

    def test_all_even_numbers(self):
        with self.assertRaises(ValueError):
            div_even_odd([2, 4, 6, 8, 10])

    def test_single_number(self):
        with self.assertRaises(ValueError):
            div_even_odd([5])

    def test_large_numbers(self):
        self.assertAlmostEqual(div_even_odd([1000000002, 1000000001]), 1.0)

    def test_negative_numbers(self):
        self.assertAlmostEqual(div_even_odd([-2, -1]), -1.0)

    def test_zero(self):
        self.assertAlmostEqual(div_even_odd([0, 1]), 0.0)
