import unittest
from mbpp_711_code import product_Equal

class TestProductEqual(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(product_Equal(30))
        self.assertTrue(product_Equal(1234))
        self.assertFalse(product_Equal(123))
        self.assertFalse(product_Equal(12345))

    def test_edge_and_boundary_conditions(self):
        self.assertFalse(product_Equal(0))
        self.assertFalse(product_Equal(1))
        self.assertTrue(product_Equal(10))
        self.assertFalse(product_Equal(11))
        self.assertTrue(product_Equal(12))

    def test_corner_cases(self):
        self.assertFalse(product_Equal(123456789))
        self.assertTrue(product_Equal(12345678))
