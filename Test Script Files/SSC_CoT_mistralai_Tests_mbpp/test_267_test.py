import unittest
from mbpp_267_code import square_Sum

class TestSquareSum(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(square_Sum(3), 36)
        self.assertEqual(square_Sum(5), 125)
        self.assertEqual(square_Sum(10), 380)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(square_Sum(0), 0)
        self.assertEqual(square_Sum(1), 1)
        self.assertEqual(square_Sum(2), 9)
        self.assertEqual(square_Sum(100), 338350)
        self.assertEqual(square_Sum(1000), 335333835)

    def test_negative_input(self):
        self.assertRaises(ValueError, square_Sum, -1)
