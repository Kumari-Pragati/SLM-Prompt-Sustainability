import unittest
from mbpp_447_code import cube_nums

class TestCubeNums(unittest.TestCase):
    def test_single_positive_number(self):
        self.assertEqual(cube_nums([1]), [1])

    def test_single_negative_number(self):
        self.assertEqual(cube_nums([-1]), [-1])

    def test_multiple_positive_numbers(self):
        self.assertEqual(cube_nums([1, 2, 3]), [1, 8, 27])

    def test_multiple_negative_numbers(self):
        self.assertEqual(cube_nums([-1, -2, -3]), [-1, -8, -27])

    def test_empty_list(self):
        self.assertEqual(cube_nums([]), [])

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            cube_nums([1, 2, '3'])
