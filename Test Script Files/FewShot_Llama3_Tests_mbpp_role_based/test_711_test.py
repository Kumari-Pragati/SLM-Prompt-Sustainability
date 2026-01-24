import unittest
from mbpp_711_code import product_Equal

class TestProductEqual(unittest.TestCase):
    def test_product_Equal_positive_numbers(self):
        self.assertTrue(product_Equal(12345))

    def test_product_Equal_negative_numbers(self):
        self.assertTrue(product_Equal(-12345))

    def test_product_Equal_single_digit(self):
        self.assertTrue(product_Equal(1))

    def test_product_Equal_zero(self):
        self.assertFalse(product_Equal(0))

    def test_product_Equal_single_digit_zero(self):
        self.assertFalse(product_Equal(0))

    def test_product_Equal_single_digit_one(self):
        self.assertTrue(product_Equal(1))

    def test_product_Equal_single_digit_two(self):
        self.assertTrue(product_Equal(2))

    def test_product_Equal_single_digit_three(self):
        self.assertTrue(product_Equal(3))

    def test_product_Equal_single_digit_four(self):
        self.assertTrue(product_Equal(4))

    def test_product_Equal_single_digit_five(self):
        self.assertTrue(product_Equal(5))

    def test_product_Equal_single_digit_six(self):
        self.assertTrue(product_Equal(6))

    def test_product_Equal_single_digit_seven(self):
        self.assertTrue(product_Equal(7))

    def test_product_Equal_single_digit_eight(self):
        self.assertTrue(product_Equal(8))

    def test_product_Equal_single_digit_nine(self):
        self.assertTrue(product_Equal(9))

    def test_product_Equal_single_digit_ten(self):
        self.assertFalse(product_Equal(10))
