import unittest
from mbpp_8_code import square_nums

class TestSquareNums(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(square_nums([1, 2, 3]), [1, 4, 9])

    def test_zero(self):
        self.assertEqual(square_nums([0]), [0])

    def test_negative_numbers(self):
        self.assertEqual(square_nums([-1, -2, -3]), [1, 4, 9])

    def test_empty_list(self):
        self.assertEqual(square_nums([]), [])

    def test_list_with_non_number(self):
        with self.assertRaises(TypeError):
            square_nums([1, 'a', 3])
