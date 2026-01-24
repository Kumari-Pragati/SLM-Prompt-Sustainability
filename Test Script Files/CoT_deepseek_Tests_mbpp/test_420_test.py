import unittest
from mbpp_420_code import cube_Sum

class TestCubeSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(cube_Sum(1), 8)
        self.assertEqual(cube_Sum(2), 144)
        self.assertEqual(cube_Sum(3), 10648)

    def test_boundary_conditions(self):
        self.assertEqual(cube_Sum(0), 0)
        self.assertEqual(cube_Sum(100), 508576710848)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            cube_Sum('a')
        with self.assertRaises(ValueError):
            cube_Sum(-1)
