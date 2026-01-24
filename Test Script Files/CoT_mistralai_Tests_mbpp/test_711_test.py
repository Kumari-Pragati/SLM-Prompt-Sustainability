import unittest
from711_code import product_Equal

class TestProductEqual(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(product_Equal(123456789))
        self.assertTrue(product_Equal(987654321))

    def test_edge_case(self):
        self.assertTrue(product_Equal(10))
        self.assertTrue(product_Equal(99))
        self.assertTrue(product_Equal(100))
        self.assertTrue(product_Equal(999))
        self.assertTrue(product_Equal(1000))
        self.assertTrue(product_Equal(9999))
        self.assertTrue(product_Equal(10000))

    def test_boundary_case(self):
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

    def test_invalid_input(self):
        self.assertRaises(TypeError, product_Equal, "not_a_number")
        self.assertRaises(TypeError, product_Equal, -1)
        self.assertRaises(TypeError, product_Equal, float("nan"))
        self.assertRaises(TypeError, product_Equal, complex(1, 2))
