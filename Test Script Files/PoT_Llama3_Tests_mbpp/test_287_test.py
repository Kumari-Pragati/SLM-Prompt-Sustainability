import unittest
from mbpp_287_code import square_Sum

class TestSquareSum(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(square_Sum(1), 1)
        self.assertEqual(square_Sum(2), 9)
        self.assertEqual(square_Sum(3), 36)

    def test_edge(self):
        self.assertEqual(square_Sum(0), 0)
        self.assertEqual(square_Sum(-1), 0)
        self.assertEqual(square_Sum(1e6), 1e12)

    def test_boundary(self):
        self.assertEqual(square_Sum(-2), 4)
        self.assertEqual(square_Sum(0), 0)
        self.assertEqual(square_Sum(1), 1)

    def test_corner(self):
        self.assertEqual(square_Sum(-3), 12)
        self.assertEqual(square_Sum(2), 9)
