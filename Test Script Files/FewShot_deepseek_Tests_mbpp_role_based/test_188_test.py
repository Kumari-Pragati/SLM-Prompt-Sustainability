import unittest
from mbpp_188_code import prod_Square

class TestProdSquare(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(prod_Square(4))
        self.assertTrue(prod_Square(16))
        self.assertTrue(prod_Square(64))

    def test_edge_case(self):
        self.assertFalse(prod_Square(1))
        self.assertFalse(prod_Square(0))
        self.assertFalse(prod_Square(-1))

    def test_boundary_case(self):
        self.assertFalse(prod_Square(2))
        self.assertFalse(prod_Square(8))
        self.assertFalse(prod_Square(15))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            prod_Square('a')
        with self.assertRaises(TypeError):
            prod_Square(None)
