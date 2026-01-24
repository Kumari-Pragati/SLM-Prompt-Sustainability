import unittest
from mbpp_8_code import square_nums

class TestSquareNums(unittest.TestCase):

    def test_square_nums_typical(self):
        self.assertEqual(square_nums([1, 2, 3, 4, 5]), [1, 4, 9, 16, 25])

    def test_square_nums_empty_list(self):
        self.assertEqual(square_nums([]), [])

    def test_square_nums_single_element(self):
        self.assertEqual(square_nums([10]), [100])

    def test_square_nums_negative_numbers(self):
        self.assertEqual(square_nums([-1, -2, -3, -4, -5]), [1, 4, 9, 16, 25])

    def test_square_nums_non_integer_input(self):
        with self.assertRaises(TypeError):
            square_nums([1, 2, '3', 4, 5])

    def test_square_nums_mixed_type_input(self):
        with self.assertRaises(TypeError):
            square_nums([1, 2, 3, 4, 5.5])
