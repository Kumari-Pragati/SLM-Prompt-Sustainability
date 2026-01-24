import unittest
from mbpp_837_code import cube_Sum

class TestCubeSum(unittest.TestCase):

    def test_cube_sum(self):
        self.assertEqual(cube_Sum(0), 0)
        self.assertEqual(cube_Sum(1), 9)
        self.assertEqual(cube_Sum(2), 36)
        self.assertEqual(cube_Sum(3), 81)
        self.assertEqual(cube_Sum(4), 144)
        self.assertEqual(cube_Sum(5), 225)
        self.assertEqual(cube_Sum(6), 324)
        self.assertEqual(cube_Sum(7), 441)
        self.assertEqual(cube_Sum(8), 576)
        self.assertEqual(cube_Sum(9), 729)

    def test_cube_sum_edge_cases(self):
        self.assertRaises(TypeError, cube_Sum, -1)
        self.assertRaises(TypeError, cube_Sum, 10.5)
