import unittest
from mbpp_38_code import div_even_odd

class TestDivEvenOdd(unittest.TestCase):
    def test_div_even_odd_positive_numbers(self):
        self.assertAlmostEqual(div_even_odd([2, 4, 6, 8, 10]), 2.0)
        self.assertAlmostEqual(div_even_odd([1, 3, 5, 7, 9]), 1.0)

    def test_div_even_odd_empty_list(self):
        self.assertRaises(ValueError, div_even_odd, [])

    def test_div_even_odd_single_even_number(self):
        self.assertRaises(ValueError, div_even_odd, [2])

    def test_div_even_odd_single_odd_number(self):
        self.assertRaises(ValueError, div_even_odd, [1])

    def test_div_even_odd_mixed_numbers(self):
        self.assertAlmostEqual(div_even_odd([2, 1, 4, 3]), 2.0)
