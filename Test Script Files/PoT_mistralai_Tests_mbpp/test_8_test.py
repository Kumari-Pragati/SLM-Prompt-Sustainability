import unittest
from mbpp_8_code import square_nums

class TestSquareNums(unittest.TestCase):

    def test_square_typical(self):
        self.assertEqual(square_nums([1, 2, 3]), [1, 4, 9])
        self.assertEqual(square_nums([-1, 0, 1]), [1, 0, 1])
        self.assertEqual(square_nums([5.5, -2.3, 0]), [30.25, 5, 0])

    def test_square_edge_cases(self):
        self.assertEqual(square_nums([]), [])
        self.assertEqual(square_nums([0]), [0])
        self.assertEqual(square_nums([float('inf')]), [float('inf')])
        self.assertEqual(square_nums([float('-inf')]), [float('-inf')])
