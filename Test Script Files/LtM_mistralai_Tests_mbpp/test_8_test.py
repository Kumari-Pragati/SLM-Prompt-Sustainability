import unittest
from mbpp_8_code import square_nums

class TestSquareNums(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(square_nums([1, 2, 3]), [1, 4, 9])

    def test_negative_numbers(self):
        self.assertEqual(square_nums([-1, -2, -3]), [1, 4, 9])

    def test_single_input(self):
        self.assertEqual(square_nums([4]), [16])

    def test_empty_list(self):
        self.assertEqual(square_nums([]), [])

    def test_float_numbers(self):
        self.assertListEqual(square_nums([1.5, 2.5]), [2.25, 6.25])

    def test_large_numbers(self):
        self.assertListEqual(square_nums([2**31 - 1, 2**31]), [2**62 - 1, 2**64])
