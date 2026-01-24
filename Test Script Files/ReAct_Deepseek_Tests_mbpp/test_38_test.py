import unittest
from mbpp_38_code import div_even_odd

class TestDivEvenOdd(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(div_even_odd([1, 2, 3, 4]), 2/1)

    def test_typical_case_with_zero(self):
        self.assertAlmostEqual(div_even_odd([0, 2, 3, 4]), 0/1)

    def test_typical_case_with_negative_numbers(self):
        self.assertAlmostEqual(div_even_odd([-1, -2, -3, -4]), -2/-1)

    def test_typical_case_with_mixed_numbers(self):
        self.assertAlmostEqual(div_even_odd([1, -2, 3, -4]), -2/1)

    def test_edge_case_with_all_odd_numbers(self):
        with self.assertRaises(ValueError):
            div_even_odd([1, 3, 5, 7])

    def test_edge_case_with_all_even_numbers(self):
        self.assertAlmostEqual(div_even_odd([2, 4, 6, 8]), 2/2)

    def test_edge_case_with_empty_list(self):
        with self.assertRaises(ValueError):
            div_even_odd([])

    def test_edge_case_with_single_element(self):
        with self.assertRaises(ValueError):
            div_even_odd([1])
