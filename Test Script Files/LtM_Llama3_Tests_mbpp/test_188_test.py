import unittest
from mbpp_188_code import prod_Square

class TestProdSquare(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(prod_Square(4))
        self.assertFalse(prod_Square(1))
        self.assertFalse(prod_Square(2))
        self.assertFalse(prod_Square(3))

    def test_edge(self):
        self.assertFalse(prod_Square(0))
        self.assertFalse(prod_Square(5))
        self.assertFalse(prod_Square(6))
        self.assertFalse(prod_Square(7))

    def test_complex(self):
        self.assertTrue(prod_Square(36))
        self.assertFalse(prod_Square(37))
        self.assertFalse(prod_Square(38))
        self.assertFalse(prod_Square(39))

    def test_invalid(self):
        with self.assertRaises(TypeError):
            prod_Square('a')
