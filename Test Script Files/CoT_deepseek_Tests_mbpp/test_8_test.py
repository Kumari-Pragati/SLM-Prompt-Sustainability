import unittest
from mbpp_8_code import square_nums

class TestSquareNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(square_nums([1, 2, 3, 4]), [1, 4, 9, 16])

    def test_empty_list(self):
        self.assertEqual(square_nums([]), [])

    def test_single_element(self):
        self.assertEqual(square_nums([5]), [25])

    def test_negative_numbers(self):
        self.assertEqual(square_nums([-1, -2, -3, -4]), [1, 4, 9, 16])

    def test_zero(self):
        self.assertEqual(square_nums([0]), [0])

    def test_large_numbers(self):
        self.assertEqual(square_nums([100, 200, 300]), [10000, 40000, 90000])

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            square_nums([1, 2, '3', 4])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            square_nums(123)
