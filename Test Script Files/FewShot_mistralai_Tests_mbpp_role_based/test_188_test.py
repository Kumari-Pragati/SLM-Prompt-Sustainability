import unittest
from mbpp_188_code import prod_Square

class TestProdSquare(unittest.TestCase):
    def test_positive_square_number(self):
        self.assertTrue(prod_Square(9))

    def test_negative_number(self):
        self.assertFalse(prod_Square(-1))

    def test_zero(self):
        self.assertFalse(prod_Square(0))

    def test_one(self):
        self.assertFalse(prod_Square(1))

    def test_non_square_number(self):
        self.assertFalse(prod_Square(10))

    def test_small_number(self):
        self.assertFalse(prod_Square(1))

    def test_large_number(self):
        self.assertTrue(prod_Square(10000))
