import unittest
from mbpp_447_code import cube_nums

class TestCubeNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(cube_nums([1, 2, 3]), [1, 8, 27])

    def test_empty_list(self):
        self.assertEqual(cube_nums([]), [])

    def test_single_element(self):
        self.assertEqual(cube_nums([5]), [125])

    def test_negative_numbers(self):
        self.assertEqual(cube_nums([-1, -2, -3]), [-1, -8, -27])

    def test_zero(self):
        self.assertEqual(cube_nums([0]), [0])

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            cube_nums([1, 2.5, 3])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            cube_nums(123)
