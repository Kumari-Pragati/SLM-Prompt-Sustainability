import unittest
from mbpp_188_code import prod_Square

class TestProdSquare(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(prod_Square(4))
        self.assertTrue(prod_Square(16))
        self.assertTrue(prod_Square(64))
        self.assertTrue(prod_Square(256))
        self.assertTrue(prod_Square(1024))

    def test_edge_cases(self):
        self.assertFalse(prod_Square(0))
        self.assertFalse(prod_Square(1))
        self.assertFalse(prod_Square(2))
        self.assertFalse(prod_Square(3))
        self.assertFalse(prod_Square(5))
        self.assertFalse(prod_Square(7))
        self.assertFalse(prod_Square(8))
        self.assertFalse(prod_Square(9))
        self.assertFalse(prod_Square(10))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            prod_Square('a')
        with self.assertRaises(TypeError):
            prod_Square(None)
        with self.assertRaises(TypeError):
            prod_Square([])
        with self.assertRaises(TypeError):
            prod_Square({})
