import unittest
from mbpp_683_code import sum_Square

class TestSumSquare(unittest.TestCase):

    def test_sum_square_true(self):
        self.assertTrue(sum_Square(5))

    def test_sum_square_false(self):
        self.assertFalse(sum_Square(10))

    def test_sum_square_true2(self):
        self.assertTrue(sum_Square(17))

    def test_sum_square_false2(self):
        self.assertFalse(sum_Square(20))

    def test_sum_square_true3(self):
        self.assertTrue(sum_Square(25))

    def test_sum_square_false3(self):
        self.assertFalse(sum_Square(30))
