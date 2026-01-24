import unittest
from mbpp_287_code import square_Sum

class TestSquareSum(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(square_Sum(1), 6)
        self.assertEqual(square_Sum(2), 24)
        self.assertEqual(square_Sum(3), 54)

    def test_edge_cases(self):
        self.assertEqual(square_Sum(0), 0)
        self.assertEqual(square_Sum(1000), 33533360)

    def test_negative_input(self):
        self.assertRaises(ValueError, square_Sum, -1)

    def test_non_integer_input(self):
        self.assertRaises(TypeError, square_Sum, 3.14)
