import unittest
from mbpp_188_code import prod_Square

class TestProdSquare(unittest.TestCase):
    def test_positive(self):
        self.assertTrue(prod_Square(9))
        self.assertTrue(prod_Square(25))
        self.assertTrue(prod_Square(49))

    def test_zero(self):
        self.assertFalse(prod_Square(0))

    def test_negative(self):
        self.assertFalse(prod_Square(-1))
        self.assertFalse(prod_Square(-4))
        self.assertFalse(prod_Square(-25))

    def test_one(self):
        self.assertFalse(prod_Square(1))

    def test_edge_cases(self):
        self.assertFalse(prod_Square(16))  # not a perfect square
        self.assertFalse(prod_Square(20))  # not a perfect square
        self.assertTrue(prod_Square(27))  # edge case: 3^3 = 27
        self.assertFalse(prod_Square(28))  # not a perfect square
