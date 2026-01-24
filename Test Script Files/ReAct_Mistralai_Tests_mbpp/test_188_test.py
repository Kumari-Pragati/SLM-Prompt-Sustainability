import unittest
from mbpp_188_code import prod_Square

class TestProdSquare(unittest.TestCase):

    def test_positive_numbers(self):
        """Test that prod_Square returns True for perfect squares"""
        for n in [4, 9, 25, 36, 49, 100]:
            self.assertTrue(prod_Square(n))

    def test_zero(self):
        """Test that prod_Square returns False for zero"""
        self.assertFalse(prod_Square(0))

    def test_negative_numbers(self):
        """Test that prod_Square returns False for negative numbers"""
        for n in [-1, -4, -9, -25]:
            self.assertFalse(prod_Square(n))

    def test_one(self):
        """Test that prod_Square returns False for 1"""
        self.assertFalse(prod_Square(1))

    def test_edge_cases(self):
        """Test that prod_Square handles edge cases correctly"""
        self.assertFalse(prod_Square(1))  # n=1 is a special case
        self.assertFalse(prod_Square(2))  # n=2 has no factors of 2
        self.assertTrue(prod_Square(3))   # n=3 is a perfect square (3*3)
        self.assertFalse(prod_Square(4))  # n=4 has no factors greater than 2
        self.assertTrue(prod_Square(5))   # n=5 is a perfect square (5*5)
        self.assertFalse(prod_Square(6))  # n=6 has no factors greater than 2
        self.assertFalse(prod_Square(7))  # n=7 has no factors of 7
        self.assertFalse(prod_Square(8))  # n=8 has no factors greater than 2
