import unittest
from mbpp_188_code import prod_Square

class TestProdSquare(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(prod_Square(9))
        self.assertTrue(prod_Square(25))
        self.assertTrue(prod_Square(49))

    def test_edge_and_boundary_cases(self):
        self.assertFalse(prod_Square(0))
        self.assertFalse(prod_Square(1))
        self.assertFalse(prod_Square(2))
        self.assertFalse(prod_Square(3))
        self.assertTrue(prod_Square(4))
        self.assertFalse(prod_Square(5))
        self.assertFalse(prod_Square(6))
        self.assertTrue(prod_Square(7))
        self.assertFalse(prod_Square(8))
        self.assertFalse(prod_Square(15))
        self.assertFalse(prod_Square(20))
        self.assertTrue(prod_Square(28))
        self.assertFalse(prod_Square(29))
        self.assertFalse(prod_Square(36))
        self.assertTrue(prod_Square(44))
        self.assertFalse(prod_Square(62))
        self.assertTrue(prod_Square(81))
