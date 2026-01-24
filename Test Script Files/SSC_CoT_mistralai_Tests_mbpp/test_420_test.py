import unittest
from mbpp_420_code import cube_Sum

class TestCubeSum(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(cube_Sum(1), 8)
        self.assertEqual(cube_Sum(2), 64)
        self.assertEqual(cube_Sum(3), 144)
        self.assertEqual(cube_Sum(4), 256)
        self.assertEqual(cube_Sum(5), 384)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(cube_Sum(0), 0)
        self.assertEqual(cube_Sum(1000), 64000000)
        self.assertEqual(cube_Sum(100000), 6400000000000)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            cube_Sum(-1)
