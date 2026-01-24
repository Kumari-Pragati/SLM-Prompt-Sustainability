import unittest
from mbpp_711_code import product_Equal

class TestProductEqual(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(product_Equal(12345))
        self.assertTrue(product_Equal(2018))
        self.assertTrue(product_Equal(1111111))

    def test_edge_cases(self):
        self.assertFalse(product_Equal(0))
        self.assertFalse(product_Equal(9))
        self.assertFalse(product_Equal(10))

    def test_corner_cases(self):
        self.assertTrue(product_Equal(11))
        self.assertTrue(product_Equal(66))
        self.assertFalse(product_Equal(252525))
