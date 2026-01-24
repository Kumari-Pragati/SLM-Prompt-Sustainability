import unittest
from mbpp_711_code import product_Equal

class TestProductEqual(unittest.TestCase):

    def test_single_digit_numbers(self):
        self.assertFalse(product_Equal(0))
        self.assertFalse(product_Equal(1))
        self.assertFalse(product_Equal(9))

    def test_two_digit_numbers(self):
        self.assertFalse(product_Equal(10))
        self.assertFalse(product_Equal(25))
        self.assertFalse(product_Equal(99))
        self.assertTrue(product_Equal(30))
        self.assertTrue(product_Equal(12))

    def test_three_digit_numbers(self):
        self.assertFalse(product_Equal(100))
        self.assertFalse(product_Equal(123))
        self.assertTrue(product_Equal(135))
        self.assertTrue(product_Equal(246))

    def test_four_digit_numbers(self):
        self.assertFalse(product_Equal(1000))
        self.assertFalse(product_Equal(1234))
        self.assertTrue(product_Equal(12345))
        self.assertTrue(product_Equal(67890))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            product_Equal('123')
        with self.assertRaises(TypeError):
            product_Equal(123.45)
        with self.assertRaises(TypeError):
            product_Equal(None)
        with self.assertRaises(TypeError):
            product_Equal([1, 2, 3])
