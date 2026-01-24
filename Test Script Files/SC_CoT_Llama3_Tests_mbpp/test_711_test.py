import unittest
from mbpp_711_code import product_Equal

class TestProductEqual(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertTrue(product_Equal(123456789))
        self.assertFalse(product_Equal(12345678))
        self.assertFalse(product_Equal(9))

    def test_edge_cases(self):
        self.assertFalse(product_Equal(10))
        self.assertFalse(product_Equal(11))
        self.assertFalse(product_Equal(12))

    def test_boundary_cases(self):
        self.assertFalse(product_Equal(999999999))
        self.assertFalse(product_Equal(1000000000))
        self.assertFalse(product_Equal(999999998))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            product_Equal('123456789')
        with self.assertRaises(TypeError):
            product_Equal(None)
        with self.assertRaises(TypeError):
            product_Equal([1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_special_cases(self):
        self.assertFalse(product_Equal(1234567890))
        self.assertFalse(product_Equal(1234567891))
