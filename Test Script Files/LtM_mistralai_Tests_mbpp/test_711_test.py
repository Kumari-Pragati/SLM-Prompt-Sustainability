import unittest
from mbpp_711_code import product_Equal

class TestProductEqual(unittest.TestCase):

    def test_simple_even(self):
        self.assertTrue(product_Equal(12))

    def test_simple_odd(self):
        self.assertTrue(product_Equal(15))

    def test_edge_min(self):
        self.assertTrue(product_Equal(9))

    def test_edge_max(self.assertFalse, self):
        self.assertFalse(product_Equal(10**100))

    def test_edge_zero(self):
        self.assertFalse(product_Equal(0))

    def test_edge_negative(self):
        self.assertFalse(product_Equal(-1))

    def test_complex_single_odd_digit(self):
        self.assertFalse(product_Equal(131))

    def test_complex_single_even_digit(self):
        self.assertTrue(product_Equal(222))

    def test_complex_mixed_digits(self):
        self.assertFalse(product_Equal(12345))
