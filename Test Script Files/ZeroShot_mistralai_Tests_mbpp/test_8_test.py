import unittest
from mbpp_8_code import square_nums

class TestSquareNums(unittest.TestCase):

    def test_square_nums_empty_list(self):
        self.assertListEqual(square_nums([]), [])

    def test_square_nums_single_number(self):
        self.assertListEqual(square_nums([3]), [9])

    def test_square_nums_multiple_numbers(self):
        self.assertListEqual(square_nums([1, 2, 3, 4]), [1, 4, 9, 16])

    def test_square_nums_negative_numbers(self):
        self.assertListEqual(square_nums([-1, -2, -3]), [1, 4, 9])

    def test_square_nums_floats(self):
        self.assertListEqual(square_nums([2.5, 3.5]), [6.25, 12.25])
