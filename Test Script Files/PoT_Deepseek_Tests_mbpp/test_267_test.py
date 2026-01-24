import unittest
from mbpp_267_code import square_Sum

class TestSquareSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(square_Sum(1), 1)
        self.assertEqual(square_Sum(2), 13)
        self.assertEqual(square_Sum(3), 44)

    def test_edge_cases(self):
        self.assertEqual(square_Sum(0), 0)
        self.assertEqual(square_Sum(-1), 1)

    def test_boundary_cases(self):
        self.assertEqual(square_Sum(100), 83333)
        self.assertEqual(square_Sum(1000), 333333333)
