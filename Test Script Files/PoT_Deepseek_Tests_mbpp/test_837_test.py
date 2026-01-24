import unittest
from mbpp_837_code import cube_Sum

class TestCubeSum(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(cube_Sum(1), 1)
        self.assertEqual(cube_Sum(2), 9 + 27)
        self.assertEqual(cube_Sum(3), 9 + 27 + 125)

    def test_edge_cases(self):
        self.assertEqual(cube_Sum(0), 0)

    def test_boundary_cases(self):
        self.assertEqual(cube_Sum(10), sum((2*i+1)**3 for i in range(10)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            cube_Sum('invalid')
