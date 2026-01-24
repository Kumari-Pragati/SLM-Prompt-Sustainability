import unittest
from mbpp_711_code import product_Equal

class TestProductEqual(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(product_Equal(3625))

    def test_edge_case(self):
        self.assertFalse(product_Equal(9))

    def test_boundary_case(self):
        self.assertFalse(product_Equal(10))
        self.assertTrue(product_Equal(111))

    def test_special_case(self):
        self.assertFalse(product_Equal(1234))
        self.assertTrue(product_Equal(13579))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            product_Equal("1234")
        with self.assertRaises(ValueError):
            product_Equal(-1234)
