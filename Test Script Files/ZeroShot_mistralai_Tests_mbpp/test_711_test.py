import unittest
from711_code import product_Equal

class TestProductEqual(unittest.TestCase):

    def test_product_equal_less_than_10(self):
        self.assertFalse(product_Equal(5))
        self.assertFalse(product_Equal(9))

    def test_product_equal_single_digit_even(self):
        self.assertTrue(product_Equal(12))
        self.assertTrue(product_Equal(22))
        self.assertTrue(product_Equal(42))
        self.assertTrue(product_Equal(62))
        self.assertTrue(product_Equal(82))

    def test_product_equal_single_digit_odd(self):
        self.assertFalse(product_Equal(13))
        self.assertFalse(product_Equal(33))
        self.assertFalse(product_Equal(53))
        self.assertFalse(product_Equal(73))
        self.assertFalse(product_Equal(93))

    def test_product_equal_two_digits_even(self):
        self.assertTrue(product_Equal(121))
        self.assertTrue(product_Equal(222))
        self.assertTrue(product_Equal(424))
        self.assertTrue(product_Equal(626))
        self.assertTrue(product_Equal(828))

    def test_product_equal_two_digits_odd(self):
        self.assertFalse(product_Equal(123))
        self.assertFalse(product_Equal(323))
        self.assertFalse(product_Equal(525))
        self.assertFalse(product_Equal(727))
        self.assertFalse(product_Equal(929))

    def test_product_equal_three_digits_even(self):
        self.assertTrue(product_Equal(1212))
        self.assertTrue(product_Equal(2222))
        self.assertTrue(product_Equal(4242))
        self.assertTrue(product_Equal(6262))
        self.assertTrue(product_Equal(8282))

    def test_product_equal_three_digits_odd(self):
        self.assertFalse(product_Equal(1213))
        self.assertFalse(product_Equal(3233))
        self.assertFalse(product_Equal(5255))
        self.assertFalse(product_Equal(7277))
        self.assertFalse(product_Equal(9299))

    def test_product_equal_four_digits_even(self):
        self.assertTrue(product_Equal(12121))
        self.assertTrue(product_Equal(22222))
        self.assertTrue(product_Equal(42424))
        self.assertTrue(product_Equal(62626))
        self.assertTrue(product_Equal(82828))

    def test_product_equal_four_digits_odd(self):
        self.assertFalse(product_Equal(12123))
        self.assertFalse(product_Equal(32323))
        self.assertFalse(product_Equal(52525))
        self.assertFalse(product_Equal(72727))
        self.assertFalse(product_Equal(92929))
