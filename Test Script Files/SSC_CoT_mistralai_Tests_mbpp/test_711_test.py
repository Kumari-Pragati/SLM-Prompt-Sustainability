import unittest
from mbpp_711_code import product_Equal

class TestProductEqual(unittest.TestCase):
    def test_normal_inputs(self):
        self.assertTrue(product_Equal(12345))
        self.assertTrue(product_Equal(22222))
        self.assertTrue(product_Equal(98764))

    def test_edge_and_boundary_conditions(self):
        self.assertFalse(product_Equal(0))
        self.assertFalse(product_Equal(9))
        self.assertFalse(product_Equal(10))
        self.assertFalse(product_Equal(11))
        self.assertFalse(product_Equal(20))
        self.assertFalse(product_Equal(30))
        self.assertFalse(product_Equal(40))
        self.assertFalse(product_Equal(50))
        self.assertFalse(product_Equal(60))
        self.assertFalse(product_Equal(70))
        self.assertFalse(product_Equal(80))
        self.assertFalse(product_Equal(90))
        self.assertTrue(product_Equal(101010))
        self.assertTrue(product_Equal(202020))
        self.assertTrue(product_Equal(303030))
        self.assertTrue(product_Equal(404040))
        self.assertTrue(product_Equal(505050))
        self.assertTrue(product_Equal(606060))
        self.assertTrue(product_Equal(707070))
        self.assertTrue(product_Equal(808080))
        self.assertTrue(product_Equal(909090))
