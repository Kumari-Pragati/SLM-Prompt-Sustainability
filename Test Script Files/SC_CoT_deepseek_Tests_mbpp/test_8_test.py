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

    def test_float_numbers(self):
        self.assertAlmostEqual(square_nums([1.5, 2.5]), [2.25, 6.25])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            square_nums('not a list')
