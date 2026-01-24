import unittest
from mbpp_420_code import cube_Sum

class TestCubeSum(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(cube_Sum(1), 8)
        self.assertEqual(cube_Sum(2), 144)
        self.assertEqual(cube_Sum(3), 784)

    def test_boundary_conditions(self):
        self.assertEqual(cube_Sum(0), 0)
        self.assertEqual(cube_Sum(10), 40000)

    def test_edge_cases(self):
        self.assertEqual(cube_Sum(-1), 0)
        self.assertEqual(cube_Sum(100), 8000000)
