import unittest
from mbpp_683_code import sum_Square

class TestSumSquare(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(sum_Square(5))
        self.assertTrue(sum_Square(10))
        self.assertTrue(sum_Square(13))
        self.assertFalse(sum_Square(1))
        self.assertFalse(sum_Square(2))
        self.assertFalse(sum_Square(3))

    def test_edge_cases(self):
        self.assertFalse(sum_Square(0))
        self.assertFalse(sum_Square(1))
        self.assertFalse(sum_Square(2))
        self.assertFalse(sum_Square(3))
        self.assertFalse(sum_Square(4))
        self.assertTrue(sum_Square(5))
        self.assertTrue(sum_Square(6))
        self.assertFalse(sum_Square(7))
        self.assertFalse(sum_Square(8))
        self.assertFalse(sum_Square(9))
        self.assertFalse(sum_Square(10))
        self.assertTrue(sum_Square(11))
        self.assertTrue(sum_Square(12))
        self.assertFalse(sum_Square(13))
        self.assertFalse(sum_Square(14))
        self.assertFalse(sum_Square(15))
        self.assertFalse(sum_Square(16))
        self.assertFalse(sum_Square(17))
        self.assertFalse(sum_Square(18))
        self.assertFalse(sum_Square(19))
        self.assertFalse(sum_Square(20))

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            sum_Square('a')
        with self.assertRaises(TypeError):
            sum_Square(None)
        with self.assertRaises(TypeError):
            sum_Square([])
