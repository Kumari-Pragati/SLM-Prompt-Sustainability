import unittest
from mbpp_420_code import cube_Sum

class TestCubeSum(unittest.TestCase):
    def test_cube_sum(self):
        self.assertEqual(cube_Sum(1), 8)
        self.assertEqual(cube_Sum(2), 64)
        self.assertEqual(cube_Sum(3), 216)
        self.assertEqual(cube_Sum(4), 512)
        self.assertEqual(cube_Sum(5), 800)

    def test_edge_cases(self):
        self.assertEqual(cube_Sum(0), 0)
        self.assertEqual(cube_Sum(1), 8)

    def test_negative_input(self):
        with self.assertRaises(TypeError):
            cube_Sum(-1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            cube_Sum('a')
