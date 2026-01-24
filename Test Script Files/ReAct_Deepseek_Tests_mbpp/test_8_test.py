import unittest
from mbpp_8_code import square_nums

class TestSquareNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(square_nums([1, 2, 3]), [1, 4, 9])

    def test_empty_list(self):
        self.assertEqual(square_nums([]), [])

    def test_negative_numbers(self):
        self.assertEqual(square_nums([-1, -2, -3]), [1, 4, 9])

    def test_zero(self):
        self.assertEqual(square_nums([0]), [0])

    def test_large_numbers(self):
        self.assertEqual(square_nums([100, 200, 300]), [10000, 40000, 90000])

    def test_decimal_numbers(self):
        self.assertEqual(square_nums([1.5, 2.5, 3.5]), [2.25, 6.25, 12.25])

    def test_non_integer_numbers(self):
        with self.assertRaises(TypeError):
            square_nums([1.5, 2, 3.5])
