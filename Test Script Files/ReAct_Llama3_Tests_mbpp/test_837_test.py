import unittest
from mbpp_837_code import cube_Sum

class TestCubeSum(unittest.TestCase):
    def test_cube_sum_positive(self):
        self.assertEqual(cube_Sum(3), 225)

    def test_cube_sum_negative(self):
        with self.assertRaises(TypeError):
            cube_Sum(-1)

    def test_cube_sum_zero(self):
        self.assertEqual(cube_Sum(0), 0)

    def test_cube_sum_small(self):
        self.assertEqual(cube_Sum(1), 1)

    def test_cube_sum_large(self):
        self.assertEqual(cube_Sum(10), 3025)
