import unittest
from mbpp_683_code import sum_Square

class TestSumSquare(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(sum_Square(5))

    def test_edge_case(self):
        self.assertFalse(sum_Square(0))
        self.assertFalse(sum_Square(1))
        self.assertFalse(sum_Square(2))
        self.assertFalse(sum_Square(3))
        self.assertFalse(sum_Square(4))

    def test_boundary_case(self):
        self.assertTrue(sum_Square(5))
        self.assertFalse(sum_Square(6))
        self.assertFalse(sum_Square(7))
        self.assertFalse(sum_Square(8))
        self.assertFalse(sum_Square(9))
        self.assertFalse(sum_Square(10))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_Square('a')
        with self.assertRaises(TypeError):
            sum_Square(None)
        with self.assertRaises(TypeError):
            sum_Square([])
