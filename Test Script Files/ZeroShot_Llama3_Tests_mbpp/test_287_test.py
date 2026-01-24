import unittest
from mbpp_287_code import square_Sum

class TestSquareSum(unittest.TestCase):

    def test_square_Sum(self):
        self.assertEqual(square_Sum(1), 1)
        self.assertEqual(square_Sum(2), 9)
        self.assertEqual(square_Sum(3), 36)
        self.assertEqual(square_Sum(4), 100)
        self.assertEqual(square_Sum(5), 225)
        self.assertEqual(square_Sum(6), 441)
        self.assertEqual(square_Sum(7), 784)
        self.assertEqual(square_Sum(8), 1331)
        self.assertEqual(square_Sum(9), 2050)
        self.assertEqual(square_Sum(10), 3025)

    def test_square_Sum_edge_cases(self):
        self.assertEqual(square_Sum(0), 0)
        self.assertEqual(square_Sum(-1), 0)
