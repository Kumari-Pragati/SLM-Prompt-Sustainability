import unittest
from mbpp_837_code import cube_Sum

class TestCubeSum(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(cube_Sum(1), 1)
        self.assertEqual(cube_Sum(2), 13)
        self.assertEqual(cube_Sum(3), 101)
        self.assertEqual(cube_Sum(4), 345)
        self.assertEqual(cube_Sum(5), 1091)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(cube_Sum(0), 0)
        self.assertEqual(cube_Sum(100), 267445)
        self.assertEqual(cube_Sum(-1), None)
        self.assertEqual(cube_Sum(2147483647), None)
