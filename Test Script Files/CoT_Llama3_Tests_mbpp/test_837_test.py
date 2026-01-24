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
        self.assertEqual(cube_Sum(10), 5625)

    def test_edge_case(self):
        self.assertEqual(cube_Sum(-1), 0)
        self.assertEqual(cube_Sum(-2), 0)
        self.assertEqual(cube_Sum(-3), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            cube_Sum('a')
