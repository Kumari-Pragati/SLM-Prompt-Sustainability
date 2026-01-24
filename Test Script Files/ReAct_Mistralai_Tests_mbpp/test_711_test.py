import unittest
from mbpp_711_code import product_Equal

class TestProductEqual(unittest.TestCase):

    def test_product_equal_for_positive_numbers(self):
        self.assertTrue(product_Equal(10))
        self.assertTrue(product_Equal(12))
        self.assertTrue(product_Equal(100))
        self.assertTrue(product_Equal(1234))
        self.assertTrue(product_Equal(9876))

    def test_product_equal_for_zero(self):
        self.assertFalse(product_Equal(0))

    def test_product_equal_for_negative_numbers(self):
        self.assertFalse(product_Equal(-1))
        self.assertFalse(product_Equal(-10))
        self.assertFalse(product_Equal(-123))
        self.assertFalse(product_Equal(-987))

    def test_product_equal_for_single_digit_numbers(self):
        self.assertFalse(product_Equal(1))
        self.assertFalse(product_Equal(2))
        self.assertFalse(product_Equal(3))
        self.assertFalse(product_Equal(4))
        self.assertFalse(product_Equal(5))
        self.assertFalse(product_Equal(6))
        self.assertFalse(product_Equal(7))
        self.assertFalse(product_Equal(8))
        self.assertFalse(product_Equal(9))
        self.assertFalse(product_Equal(10))  # Already tested in positive numbers

    def test_product_equal_for_large_numbers(self):
        self.assertTrue(product_Equal(123456789))
        self.assertTrue(product_Equal(987654321))
