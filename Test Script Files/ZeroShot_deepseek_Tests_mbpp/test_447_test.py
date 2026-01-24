import unittest
from mbpp_447_code import cube_nums

class TestCubeNums(unittest.TestCase):

    def test_cube_nums(self):
        self.assertEqual(cube_nums([1, 2, 3]), [1, 8, 27])
        self.assertEqual(cube_nums([-1, -2, -3]), [-1, -8, -27])
        self.assertEqual(cube_nums([0]), [0])
        self.assertEqual(cube_nums([]), [])
