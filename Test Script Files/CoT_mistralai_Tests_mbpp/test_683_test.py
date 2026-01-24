import unittest
from mbpp_683_code import sum_Square

class TestSumSquare(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertTrue(sum_Square(1))
        self.assertTrue(sum_Square(5))
        self.assertTrue(sum_Square(8))
        self.assertTrue(sum_Square(9))
        self.assertTrue(sum_Square(10))
        self.assertTrue(sum_Square(25))

    def test_zero(self):
        self.assertFalse(sum_Square(0))

    def test_negative_numbers(self):
        self.assertFalse(sum_Square(-1))
        self.assertFalse(sum_Square(-2))
        self.assertFalse(sum_Square(-3))
        self.assertFalse(sum_Square(-4))
        self.assertFalse(sum_Square(-5))

    def test_edge_cases(self):
        self.assertTrue(sum_Square(1*1))
        self.assertTrue(sum_Square(2*2))
        self.assertFalse(sum_Square(3*3))
        self.assertTrue(sum_Square(4*4))
        self.assertTrue(sum_Square(5*5))
        self.assertFalse(sum_Square(6*6))

    def test_large_numbers(self):
        self.assertTrue(sum_Square(289))
        self.assertFalse(sum_Square(290))
        self.assertTrue(sum_Square(4489))
