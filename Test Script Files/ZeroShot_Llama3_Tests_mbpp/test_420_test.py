import unittest
from mbpp_420_code import cube_Sum

class TestCubeSum(unittest.TestCase):

    def test_cube_sum(self):
        self.assertEqual(cube_Sum(1), 8)
        self.assertEqual(cube_Sum(2), 64)
        self.assertEqual(cube_Sum(3), 144)
        self.assertEqual(cube_Sum(4), 256)
        self.assertEqual(cube_Sum(5), 400)
        self.assertEqual(cube_Sum(6), 576)
        self.assertEqual(cube_Sum(7), 784)
        self.assertEqual(cube_Sum(8), 1024)
        self.assertEqual(cube_Sum(9), 1296)
        self.assertEqual(cube_Sum(10), 1600)

    def test_cube_sum_edge_cases(self):
        self.assertEqual(cube_Sum(0), 0)
        self.assertEqual(cube_Sum(-1), 0)
