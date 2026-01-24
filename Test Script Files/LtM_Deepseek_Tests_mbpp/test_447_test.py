import unittest
from mbpp_447_code import cube_nums

class TestCubeNums(unittest.TestCase):
    def test_cube_nums_simple(self):
        self.assertEqual(cube_nums([1, 2, 3]), [1, 8, 27])

    def test_cube_nums_empty(self):
        self.assertEqual(cube_nums([]), [])

    def test_cube_nums_negative(self):
        self.assertEqual(cube_nums([-1, -2, -3]), [-1, -8, -27])

    def test_cube_nums_zero(self):
        self.assertEqual(cube_nums([0]), [0])

    def test_cube_nums_large_numbers(self):
        self.assertEqual(cube_nums([100, 200, 300]), [1000000, 800000000, 270000000000])
