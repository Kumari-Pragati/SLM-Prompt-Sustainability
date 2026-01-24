import unittest
from mbpp_837_code import cube_Sum

class TestCubeSum(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(cube_Sum(1), 1)
        self.assertEqual(cube_Sum(2), 9)
        self.assertEqual(cube_Sum(3), 36)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(cube_Sum(0), 0)
        self.assertEqual(cube_Sum(4), 100)
        self.assertEqual(cube_Sum(5), 225)

    def test_negative_input(self):
        self.assertRaises(ValueError, cube_Sum, -1)

    def test_large_input(self):
        self.assertEqual(cube_Sum(1000), 167960361)
