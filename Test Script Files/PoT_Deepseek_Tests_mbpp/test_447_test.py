import unittest
from mbpp_447_code import cube_nums

class TestCubeNums(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(cube_nums([1, 2, 3]), [1, 8, 27])
        self.assertEqual(cube_nums([-1, -2, -3]), [-1, -8, -27])
        self.assertEqual(cube_nums([0]), [0])

    def test_edge_cases(self):
        self.assertEqual(cube_nums([]), [])
        self.assertEqual(cube_nums([1]), [1])
        self.assertEqual(cube_nums([-1]), [-1])

    def test_corner_cases(self):
        self.assertEqual(cube_nums([10]), [1000])
        self.assertEqual(cube_nums([-10]), [-1000])
        self.assertEqual(cube_nums([0.5]), [0.125])
        self.assertEqual(cube_nums([-0.5]), [-0.125])
