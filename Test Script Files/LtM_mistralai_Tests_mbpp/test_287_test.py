import unittest
from mbpp_287_code import square_Sum

class TestSquareSum(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(square_Sum(1), 6)
        self.assertEqual(square_Sum(2), 28)
        self.assertEqual(square_Sum(3), 81)

    def test_edge_input(self):
        self.assertEqual(square_Sum(0), 0)
        self.assertEqual(square_Sum(1000), 33533360)

    def test_negative_input(self):
        self.assertRaises(ValueError, square_Sum, -1)

    def test_float_input(self):
        self.assertRaises(TypeError, square_Sum, 2.5)
