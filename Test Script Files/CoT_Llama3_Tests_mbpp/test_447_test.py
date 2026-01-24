import unittest
from mbpp_447_code import cube_nums

class TestCubeNums(unittest.TestCase):
    def test_cube_nums_typical(self):
        self.assertEqual(cube_nums([1, 2, 3]), [1, 8, 27])

    def test_cube_nums_edge(self):
        self.assertEqual(cube_nums([-1, 0, 1]), [-1, 0, 1])

    def test_cube_nums_negative(self):
        self.assertEqual(cube_nums([-2, -3, -4]), [8, 27, 64])

    def test_cube_nums_empty(self):
        self.assertEqual(cube_nums([]), [])

    def test_cube_nums_single(self):
        self.assertEqual(cube_nums([5]), [125])

    def test_cube_nums_multiple_negative(self):
        self.assertEqual(cube_nums([-1, -2, -3]), [1, 8, 27])

    def test_cube_nums_multiple_positive(self):
        self.assertEqual(cube_nums([1, 2, 3]), [1, 8, 27])
