import unittest
from mbpp_447_code import cube_nums

class TestCubeNums(unittest.TestCase):

    def test_cube_nums(self):
        self.assertEqual(cube_nums([1, 2, 3]), [1, 8, 27])
        self.assertEqual(cube_nums([-1, -2, -3]), [-1, -8, -27])
        self.assertEqual(cube_nums([0, 0, 0]), [0, 0, 0])
        self.assertEqual(cube_nums([-1, 0, 1]), [-1, 0, 1])
        self.assertEqual(cube_nums([-2, -1, 0, 1, 2]), [-8, -1, 0, 1, 8])

    def test_cube_nums_empty_list(self):
        self.assertEqual(cube_nums([]), [])
