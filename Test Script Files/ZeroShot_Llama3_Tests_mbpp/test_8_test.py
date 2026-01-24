import unittest
from mbpp_8_code import square_nums

class TestSquareNums(unittest.TestCase):

    def test_square_nums(self):
        self.assertEqual(square_nums([1, 2, 3]), [1, 4, 9])
        self.assertEqual(square_nums([-1, -2, -3]), [1, 4, 9])
        self.assertEqual(square_nums([0, 0, 0]), [0, 0, 0])
        self.assertEqual(square_nums([-1, 0, 1]), [1, 0, 1])
        self.assertEqual(square_nums([-2, -1, 0, 1, 2]), [4, 1, 0, 1, 4])

    def test_square_nums_empty_list(self):
        self.assertEqual(square_nums([]), [])

    def test_square_nums_single_element(self):
        self.assertEqual(square_nums([5]), [25])
