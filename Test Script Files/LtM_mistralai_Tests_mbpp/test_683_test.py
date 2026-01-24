import unittest
from mbpp_683_code import sum_Square

class TestSumSquare(unittest.TestCase):

    def test_simple(self):
        self.assertTrue(sum_Square(4))
        self.assertTrue(sum_Square(9))
        self.assertFalse(sum_Square(0))
        self.assertFalse(sum_Square(1))
        self.assertFalse(sum_Square(2))
        self.assertFalse(sum_Square(3))
        self.assertFalse(sum_Square(5))
        self.assertFalse(sum_Square(6))
        self.assertFalse(sum_Square(7))
        self.assertFalse(sum_Square(8))
        self.assertFalse(sum_Square(10))

    def test_edge_and_boundary(self):
        self.assertTrue(sum_Square(16))
        self.assertTrue(sum_Square(25))
        self.assertFalse(sum_Square(26))
        self.assertFalse(sum_Square(27))
        self.assertFalse(sum_Square(28))
        self.assertFalse(sum_Square(29))
        self.assertTrue(sum_Square(36))
        self.assertTrue(sum_Square(49))
        self.assertFalse(sum_Square(64))
        self.assertFalse(sum_Square(81))
        self.assertFalse(sum_Square(100))
        self.assertFalse(sum_Square(121))
        self.assertFalse(sum_Square(144))
        self.assertFalse(sum_Square(169))
        self.assertFalse(sum_Square(196))
        self.assertFalse(sum_Square(225))
