import unittest
from mbpp_38_code import div_even_odd

class TestDivEvenOdd(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(div_even_odd([2, 3, 4, 5]), 2/3)

    def test_edge_case_zero_dividend(self):
        self.assertRaises(ZeroDivisionError, div_even_odd, [2, 4, 6])

    def test_edge_case_zero_divisor(self):
        self.assertRaises(ZeroDivisionError, div_even_odd, [0, 2, 4])

    def test_edge_case_single_element(self):
        self.assertRaises(ValueError, div_even_odd, [2])

    def test_edge_case_empty_list(self):
        self.assertRaises(ValueError, div_even_odd, [])

    def test_edge_case_multiple_zeros(self):
        self.assertRaises(ZeroDivisionError, div_even_odd, [0, 0, 2, 4])

    def test_edge_case_multiple_evens(self):
        self.assertAlmostEqual(div_even_odd([2, 4, 6, 8]), 2/4)

    def test_edge_case_multiple_odds(self):
        self.assertAlmostEqual(div_even_odd([1, 3, 5, 7]), 1/3)
