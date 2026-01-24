import unittest
from mbpp_420_code import cube_Sum

class TestCubeSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(cube_Sum(1), 8)
        self.assertEqual(cube_Sum(2), 144)
        self.assertEqual(cube_Sum(3), 1040)

    def test_edge_cases(self):
        self.assertEqual(cube_Sum(0), 0)

    def test_boundary_cases(self):
        self.assertEqual(cube_Sum(10), 800000)
        self.assertEqual(cube_Sum(100), 8000000000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            cube_Sum('a')
        with self.assertRaises(TypeError):
            cube_Sum(None)
        with self.assertRaises(TypeError):
            cube_Sum([])
