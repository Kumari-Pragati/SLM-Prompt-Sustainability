import unittest
from mbpp_837_code import cube_Sum

class TestCubeSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(cube_Sum(1), 1)
        self.assertEqual(cube_Sum(2), 9 + 27)
        self.assertEqual(cube_Sum(3), 9 + 27 + 125)

    def test_boundary_conditions(self):
        self.assertEqual(cube_Sum(0), 0)
        self.assertEqual(cube_Sum(100), sum((2*i+1)**3 for i in range(100)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            cube_Sum('a')
        with self.assertRaises(ValueError):
            cube_Sum(-1)
