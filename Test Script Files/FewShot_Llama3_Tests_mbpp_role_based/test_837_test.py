import unittest
from mbpp_837_code import cube_Sum

class TestCubeSum(unittest.TestCase):
    def test_cube_sum_of_positive_numbers(self):
        self.assertEqual(cube_Sum(5), 385)

    def test_cube_sum_of_zero(self):
        self.assertEqual(cube_Sum(0), 0)

    def test_cube_sum_of_negative_numbers(self):
        self.assertEqual(cube_Sum(-5), 385)

    def test_cube_sum_of_non_integer(self):
        with self.assertRaises(TypeError):
            cube_Sum(5.5)
