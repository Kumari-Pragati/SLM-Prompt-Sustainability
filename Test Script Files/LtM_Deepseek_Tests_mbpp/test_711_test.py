import unittest
from mbpp_711_code import product_Equal

class TestProductEqual(unittest.TestCase):

    def test_single_digit_numbers(self):
        self.assertFalse(product_Equal(0))
        self.assertFalse(product_Equal(1))
        self.assertFalse(product_Equal(2))
        self.assertFalse(product_Equal(3))
        self.assertFalse(product_Equal(4))
        self.assertFalse(product_Equal(5))
        self.assertFalse(product_Equal(6))
        self.assertFalse(product_Equal(7))
        self.assertFalse(product_Equal(8))
        self.assertFalse(product_Equal(9))

    def test_two_digits_numbers(self):
        self.assertTrue(product_Equal(10))
        self.assertFalse(product_Equal(11))
        self.assertFalse(product_Equal(12))
        self.assertFalse(product_Equal(13))
        self.assertFalse(product_Equal(14))
        self.assertFalse(product_Equal(15))
        self.assertFalse(product_Equal(16))
        self.assertFalse(product_Equal(17))
        self.assertFalse(product_Equal(18))
        self.assertFalse(product_Equal(19))
        self.assertFalse(product_Equal(20))

    def test_three_digits_numbers(self):
        self.assertTrue(product_Equal(210))
        self.assertFalse(product_Equal(211))
        self.assertFalse(product_Equal(212))
        self.assertFalse(product_Equal(213))
        self.assertFalse(product_Equal(214))
        self.assertFalse(product_Equal(215))
        self.assertFalse(product_Equal(216))
        self.assertFalse(product_Equal(217))
        self.assertFalse(product_Equal(218))
        self.assertFalse(product_Equal(219))

    def test_four_digits_numbers(self):
        self.assertTrue(product_Equal(1234))
        self.assertFalse(product_Equal(1235))
        self.assertFalse(product_Equal(1236))
        self.assertFalse(product_Equal(1237))
        self.assertFalse(product_Equal(1238))
        self.assertFalse(product_Equal(1239))

    def test_five_digits_numbers(self):
        self.assertTrue(product_Equal(12345))
        self.assertFalse(product_Equal(12346))
        self.assertFalse(product_Equal(12347))
        self.assertFalse(product_Equal(12348))
        self.assertFalse(product_Equal(12349))

    def test_six_digits_numbers(self):
        self.assertTrue(product_Equal(123456))
        self.assertFalse(product_Equal(123457))
        self.assertFalse(product_Equal(123458))
        self.assertFalse(product_Equal(123459))

    def test_seven_digits_numbers(self):
        self.assertTrue(product_Equal(1234567))
        self.assertFalse(product_Equal(1234568))
        self.assertFalse(product_Equal(1234569))

    def test_eight_digits_numbers(self):
        self.assertTrue(product_Equal(12345678))
        self.assertFalse(product_Equal(12345679))

    def test_nine_digits_numbers(self):
        self.assertTrue(product_Equal(123456789))
