import unittest
from mbpp_711_code import product_Equal

class TestProductEqual(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertFalse(product_Equal(5))
        self.assertFalse(product_Equal(9))
        self.assertTrue(product_Equal(10))
        self.assertFalse(product_Equal(11))
        self.assertTrue(product_Equal(12))

    def test_edge_and_boundary_conditions(self):
        self.assertFalse(product_Equal(0))
        self.assertFalse(product_Equal(1))
        self.assertFalse(product_Equal(2))
        self.assertFalse(product_Equal(3))
        self.assertFalse(product_Equal(4))

    def test_complex_and_corner_cases(self):
        self.assertFalse(product_Equal(15))
        self.assertFalse(product_Equal(16))
        self.assertFalse(product_Equal(17))
        self.assertFalse(product_Equal(18))
        self.assertFalse(product_Equal(19))
