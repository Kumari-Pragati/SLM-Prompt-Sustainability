import unittest
from mbpp_8_code import square_nums

class TestSquareNums(unittest.TestCase):
    def test_square_nums(self):
        self.assertEqual(square_nums([1, 2, 3, 4, 5]), [1, 4, 9, 16, 25])
        self.assertEqual(square_nums([-1, -2, -3, -4, -5]), [1, 4, 9, 16, 25])
        self.assertEqual(square_nums([0]), [0])
        self.assertEqual(square_nums([]), [])
