import unittest
from mbpp_8_code import square_nums

class TestSquareNums(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(square_nums([1, 2, 3]), [1, 4, 9])
        self.assertEqual(square_nums([-1, -2, -3]), [1, 4, 9])
        self.assertEqual(square_nums([0, 0, 0]), [0, 0, 0])

    def test_edge_cases(self):
        self.assertEqual(square_nums([]), [])
        self.assertEqual(square_nums([1]), [1])

    def test_corner_cases(self):
        self.assertEqual(square_nums([100]), [10000])
        self.assertEqual(square_nums([-100]), [10000])
