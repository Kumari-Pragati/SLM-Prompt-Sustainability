import unittest
from mbpp_261_code import division_elements

class TestDivisionElements(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(division_elements((10, 2), (5, 1)), (5, 2.5))

    def test_edge_case_zero_divisor(self):
        with self.assertRaises(ZeroDivisionError):
            division_elements((10, 0), (5, 1))

    def test_edge_case_zero_dividend(self):
        self.assertEqual(division_elements((0, 2), (5, 1)), (0, 0))

    def test_edge_case_divisor_zero(self):
        with self.assertRaises(ZeroDivisionError):
            division_elements((10, 2), (0, 1))

    def test_edge_case_dividend_zero(self):
        self.assertEqual(division_elements((0, 2), (0, 1)), (0, 0))

    def test_edge_case_divisor_and_dividend_zero(self):
        with self.assertRaises(ZeroDivisionError):
            division_elements((0, 0), (0, 1))

    def test_edge_case_divisor_and_dividend_negative(self):
        self.assertEqual(division_elements((-10, -2), (-5, -1)), (2, 2))

    def test_edge_case_divisor_and_dividend_positive(self):
        self.assertEqual(division_elements((10, 2), (5, 1)), (2, 2))

    def test_edge_case_divisor_and_dividend_mixed(self):
        self.assertEqual(division_elements((-10, 2), (5, 1)), (-2, 2))

    def test_edge_case_divisor_and_dividend_mixed_with_zero(self):
        self.assertEqual(division_elements((-10, 0), (5, 1)), (0, 0))

    def test_edge_case_divisor_and_dividend_mixed_with_zero_divisor(self):
        with self.assertRaises(ZeroDivisionError):
            division_elements((-10, 0), (0, 1))

    def test_edge_case_divisor_and_dividend_mixed_with_zero_dividend(self):
        self.assertEqual(division_elements((0, 2), (0, 1)), (0, 0))
