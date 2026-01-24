import unittest
from mbpp_8_code import square_nums

class TestSquareNums(unittest.TestCase):
    def test_square_positive_numbers(self):
        self.assertEqual(square_nums([1, 2, 3, 4, 5]), [1, 4, 9, 16, 25])

    def test_square_negative_numbers(self):
        self.assertEqual(square_nums([-1, -2, -3, -4, -5]), [1, 4, 9, 16, 25])

    def test_square_zero(self):
        self.assertEqual(square_nums([0]), [0])

    def test_square_empty_list(self):
        self.assertEqual(square_nums([]), [])

    def test_square_non_numeric_input(self):
        with self.assertRaises(TypeError):
            square_nums(['a', 'b', 'c'])
