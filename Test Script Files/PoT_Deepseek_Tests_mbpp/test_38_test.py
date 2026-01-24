import unittest
from mbpp_38_code import div_even_odd

class TestDivEvenOdd(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(div_even_odd([2, 4, 6, 8, 10]), 0.5)

    def test_edge_case_with_single_even(self):
        self.assertEqual(div_even_odd([2]), -1)

    def test_edge_case_with_single_odd(self):
        self.assertEqual(div_even_odd([1]), -1)

    def test_edge_case_with_no_even_no_odd(self):
        self.assertEqual(div_even_odd([3, 5, 7]), -1)

    def test_boundary_case_with_empty_list(self):
        self.assertEqual(div_even_odd([]), -1)

    def test_corner_case_with_negative_numbers(self):
        self.assertAlmostEqual(div_even_odd([-2, -4, -6, -8, -10]), 0.5)

    def test_corner_case_with_mixed_positive_negative(self):
        self.assertAlmostEqual(div_even_odd([-2, 4, -6, 8, -10]), -0.5)

    def test_corner_case_with_mixed_positive_negative_odd_even(self):
        self.assertAlmostEqual(div_even_odd([-1, 2, -3, 4, -5]), 0.5)
