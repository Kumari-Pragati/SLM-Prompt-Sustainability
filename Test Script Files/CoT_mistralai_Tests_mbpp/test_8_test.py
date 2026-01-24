import unittest
from mbpp_8_code import square_nums

class TestSquareNums(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(square_nums([]), [])

    def test_single_number(self):
        self.assertListEqual(square_nums([3]), [9])

    def test_positive_numbers(self):
        self.assertListEqual(square_nums([1, 2, 3, 4, 5]), [1, 4, 9, 16, 25])

    def test_negative_numbers(self):
        self.assertListEqual(square_nums([-1, -2, -3]), [1, 4, 9])

    def test_mixed_numbers(self):
        self.assertListEqual(square_nums([1, -2, 3, -4, 5]), [1, 4, 9, 16, 25])

    def test_floats(self):
        self.assertListEqual(square_nums([2.5, 3.5]), [6.25, 12.25])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            square_nums('string')
