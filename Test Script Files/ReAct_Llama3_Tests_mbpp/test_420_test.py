import unittest
from mbpp_420_code import cube_Sum

class TestCubeSum(unittest.TestCase):
    def test_cube_sum_positive(self):
        self.assertEqual(cube_Sum(5), 980)

    def test_cube_sum_negative(self):
        with self.assertRaises(TypeError):
            cube_Sum(-1)

    def test_cube_sum_zero(self):
        self.assertEqual(cube_Sum(0), 0)

    def test_cube_sum_one(self):
        self.assertEqual(cube_Sum(1), 0)

    def test_cube_sum_large(self):
        self.assertEqual(cube_Sum(100), 9800000)
