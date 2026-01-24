import unittest
from mbpp_711_code import product_Equal

class TestProductEqual(unittest.TestCase):
    def test_single_digit_number(self):
        self.assertFalse(product_Equal(1))

    def test_two_digits_number_equal_product(self):
        self.assertTrue(product_Equal(25))

    def test_two_digits_number_unequal_product(self):
        self.assertFalse(product_Equal(24))

    def test_three_digits_number_equal_product(self):
        self.assertTrue(product_Equal(307))

    def test_three_digits_number_unequal_product(self):
        self.assertFalse(product_Equal(306))

    def test_large_number_equal_product(self):
        self.assertTrue(product_Equal(123456789))

    def test_large_number_unequal_product(self):
        self.assertFalse(product_Equal(123456788))

    def test_zero(self):
        self.assertFalse(product_Equal(0))

    def test_negative_number(self):
        self.assertFalse(product_Equal(-12345))
