import unittest
from mbpp_837_code import cube_Sum

class TestCubeSum(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(cube_Sum(1), 1)
        self.assertEqual(cube_Sum(2), 9)
        self.assertEqual(cube_Sum(3), 36)
        self.assertEqual(cube_Sum(4), 81)
        self.assertEqual(cube_Sum(5), 125)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(cube_Sum(0), 0)
        self.assertEqual(cube_Sum(6), 297)
        self.assertEqual(cube_Sum(7), 561)
        self.assertEqual(cube_Sum(8), 1028)
        self.assertEqual(cube_Sum(9), 1629)
