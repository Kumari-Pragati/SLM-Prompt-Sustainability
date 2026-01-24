import unittest
from mbpp_711_code import product_Equal

class TestProductEqual(unittest.TestCase):

    def test_single_digit_numbers(self):
        self.assertFalse(product_Equal(0))
        self.assertFalse(product_Equal(1))
        self.assertFalse(product_Equal(9))

    def test_two_digit_numbers(self):
        self.assertFalse(product_Equal(10))
        self.assertFalse(product_Equal(11))
        self.assertFalse(product_Equal(19))
        self.assertFalse(product_Equal(90))
        self.assertFalse(product_Equal(91))
        self.assertFalse(product_Equal(99))

    def test_three_digit_numbers(self):
        self.assertFalse(product_Equal(100))
        self.assertFalse(product_Equal(101))
        self.assertFalse(product_Equal(110))
        self.assertFalse(product_Equal(111))
        self.assertFalse(product_Equal(190))
        self.assertFalse(product_Equal(191))
        self.assertFalse(product_Equal(900))
        self.assertFalse(product_Equal(901))
        self.assertFalse(product_Equal(910))
        self.assertFalse(product_Equal(911))
        self.assertFalse(product_Equal(990))
        self.assertFalse(product_Equal(991))
        self.assertFalse(product_Equal(999))

    def test_large_numbers(self):
        self.assertFalse(product_Equal(1000))
        self.assertFalse(product_Equal(1001))
        self.assertFalse(product_Equal(1100))
        self.assertFalse(product_Equal(1110))
        self.assertFalse(product_Equal(1111))
        self.assertFalse(product_Equal(1900))
        self.assertFalse(product_Equal(1901))
        self.assertFalse(product_Equal(1910))
        self.assertFalse(product_Equal(1911))
        self.assertFalse(product_Equal(9000))
        self.assertFalse(product_Equal(9001))
        self.assertFalse(product_Equal(9010))
        self.assertFalse(product_Equal(9011))
        self.assertFalse(product_Equal(9100))
        self.assertFalse(product_Equal(9101))
        self.assertFalse(product_Equal(9110))
        self.assertFalse(product_Equal(9111))
        self.assertFalse(product_Equal(9900))
        self.assertFalse(product_Equal(9901))
        self.assertFalse(product_Equal(9910))
        self.assertFalse(product_Equal(9911))
        self.assertFalse(product_Equal(9990))
        self.assertFalse(product_Equal(9991))
        self.assertFalse(product_Equal(9999))
