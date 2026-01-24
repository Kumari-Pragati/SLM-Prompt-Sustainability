import unittest
from mbpp_188_code import prod_Square

class TestProdSquare(unittest.TestCase):
    def test_normal(self):
        self.assertTrue(prod_Square(9))
        self.assertTrue(prod_Square(25))
        self.assertTrue(prod_Square(49))

    def test_edge_cases(self):
        self.assertFalse(prod_Square(0))
        self.assertFalse(prod_Square(1))
        self.assertFalse(prod_Square(2))
        self.assertFalse(prod_Square(3))

    def test_boundary_cases(self):
        self.assertTrue(prod_Square(4))
        self.assertTrue(prod_Square(16))
        self.assertFalse(prod_Square(20))
        self.assertTrue(prod_Square(27))

    def test_special_cases(self):
        self.assertTrue(prod_Square(10))  # 2*2*5*5 = 10
        self.assertFalse(prod_Square(11))  # No square number can be multiplied to give 11
        self.assertTrue(prod_Square(26))  # 2*3*7*7 = 26
        self.assertFalse(prod_Square(28))  # No square number can be multiplied to give 28
