import unittest
from mbpp_711_code import product_Equal

class TestProductEqual(unittest.TestCase):

    def test_product_Equal_less_than_10(self):
        self.assertFalse(product_Equal(9))

    def test_product_Equal_equal_digits(self):
        self.assertTrue(product_Equal(2345))

    def test_product_Equal_unequal_digits(self):
        self.assertFalse(product_Equal(2346))

    def test_product_Equal_single_digit(self):
        self.assertFalse(product_Equal(1))

    def test_product_Equal_zero(self):
        self.assertFalse(product_Equal(0))

    def test_product_Equal_negative_number(self):
        self.assertFalse(product_Equal(-1234))

    def test_product_Equal_large_number(self):
        self.assertTrue(product_Equal(123456789))
