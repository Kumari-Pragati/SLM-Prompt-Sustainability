import unittest
from mbpp_188_code import prod_Square

class TestProdSquare(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(prod_Square(9))
        self.assertFalse(prod_Square(4))
        self.assertFalse(prod_Square(0))
        self.assertFalse(prod_Square(1))

    def test_edge_cases(self):
        self.assertTrue(prod_Square(16))
        self.assertFalse(prod_Square(25))
        self.assertTrue(prod_Square(28))
        self.assertFalse(prod_Square(29))

    def test_complex(self):
        self.assertTrue(prod_Square(2704))
        self.assertFalse(prod_Square(2705))
        self.assertTrue(prod_Square(4096))
        self.assertFalse(prod_Square(4097))
