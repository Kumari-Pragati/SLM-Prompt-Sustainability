import unittest
from mbpp_683_code import sum_Square

class TestSumSquare(unittest.TestCase):

    def test_sum_square_positive(self):
        self.assertTrue(sum_Square(5))
        self.assertTrue(sum_Square(9))
        self.assertTrue(sum_Square(12))
        self.assertTrue(sum_Square(20))
        self.assertTrue(sum_Square(28))

    def test_sum_square_zero(self):
        self.assertFalse(sum_Square(0))
        self.assertFalse(sum_Square(1))
        self.assertFalse(sum_Square(2))
        self.assertFalse(sum_Square(3))
        self.assertFalse(sum_Square(4))

    def test_sum_square_negative(self):
        self.assertFalse(sum_Square(-1))
        self.assertFalse(sum_Square(-4))
        self.assertFalse(sum_Square(-9))
        self.assertFalse(sum_Square(-16))
        self.assertFalse(sum_Square(-25))

    def test_sum_square_edge_cases(self):
        self.assertTrue(sum_Square(8))
        self.assertTrue(sum_Square(25))
        self.assertTrue(sum_Square(625))
        self.assertFalse(sum_Square(7))
        self.assertFalse(sum_Square(26))
        self.assertFalse(sum_Square(27))
