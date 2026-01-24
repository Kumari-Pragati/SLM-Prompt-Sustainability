import unittest
from mbpp_447_code import cube_nums

class TestCubeNums(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(cube_nums([1, 2, 3]), [1, 8, 27])

    def test_negative_input(self):
        self.assertEqual(cube_nums([-1, -2, -3]), [1, 8, 27])

    def test_zero_input(self):
        self.assertEqual(cube_nums([0]), [0])

    def test_float_input(self):
        self.assertEqual(cube_nums([1.5, 2.5, 3.5]), [3.375, 125.0, 229.25])

    def test_empty_input(self):
        self.assertEqual(cube_nums([]), [])

    def test_single_input(self):
        self.assertEqual(cube_nums([4]), [64])
