import unittest
from mbpp_267_code import square_Sum

class TestSquareSum(unittest.TestCase):

    def test_square_Sum(self):
        self.assertEqual(square_Sum(1), 1)
        self.assertEqual(square_Sum(2), 4)
        self.assertEqual(square_Sum(3), 25)
        self.assertEqual(square_Sum(4), 100)
        self.assertEqual(square_Sum(5), 225)
        self.assertEqual(square_Sum(6), 361)
        self.assertEqual(square_Sum(7), 625)
        self.assertEqual(square_Sum(8), 1000)
        self.assertEqual(square_Sum(9), 1225)
        self.assertEqual(square_Sum(10), 1461)

    def test_square_Sum_edge_cases(self):
        self.assertRaises(TypeError, square_Sum, 'a')
        self.assertRaises(TypeError, square_Sum, None)
        self.assertRaises(TypeError, square_Sum, [])
