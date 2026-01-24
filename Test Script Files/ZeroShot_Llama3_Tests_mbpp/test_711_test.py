import unittest
from mbpp_711_code import product_Equal

class TestProductEqual(unittest.TestCase):

    def test_product_Equal_positive(self):
        self.assertTrue(product_Equal(12345))
        self.assertTrue(product_Equal(24680))
        self.assertTrue(product_Equal(13579))
        self.assertTrue(product_Equal(98765))

    def test_product_Equal_negative(self):
        self.assertFalse(product_Equal(-12345))
        self.assertFalse(product_Equal(-24680))
        self.assertFalse(product_Equal(-13579))
        self.assertFalse(product_Equal(-98765))

    def test_product_Equal_zero(self):
        self.assertFalse(product_Equal(0))

    def test_product_Equal_single_digit(self):
        self.assertFalse(product_Equal(1))
        self.assertFalse(product_Equal(2))
        self.assertFalse(product_Equal(3))
        self.assertFalse(product_Equal(4))
        self.assertFalse(product_Equal(5))
        self.assertFalse(product_Equal(6))
        self.assertFalse(product_Equal(7))
        self.assertFalse(product_Equal(8))
        self.assertFalse(product_Equal(9))

    def test_product_Equal_greater_than_10(self):
        self.assertTrue(product_Equal(123456789))
        self.assertTrue(product_Equal(246810987))
        self.assertTrue(product_Equal(135790123))
        self.assertTrue(product_Equal(987654321))
