import unittest
from mbpp_784_code import mul_even_odd

class TestMulEvenOdd(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(mul_even_odd([2, 3, 4, 5, 6]), 24)
        self.assertEqual(mul_even_odd([-2, -3, 4, 5, -6]), 24)
        self.assertEqual(mul_even_odd([2, -3, 4, -5, 6]), -24)

    def test_edge_case_empty_list(self):
        self.assertIs(mul_even_odd([]), -1)

    def test_edge_case_single_element(self):
        self.assertIs(mul_even_odd([1]), -1)
        self.assertIs(mul_even_odd([2]), 2)
        self.assertIs(mul_even_odd([-2]), -2)

    def test_corner_case_odd_length(self):
        self.assertIs(mul_even_odd([2, 3, 4]), -1)
        self.assertIs(mul_even_odd([-2, -3, 4]), -12)
        self.assertIs(mul_even_odd([2, -3, -4]), 24)
