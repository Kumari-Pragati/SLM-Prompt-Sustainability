import unittest
from mbpp_420_code import cube_Sum

class TestCubeSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(cube_Sum(5), 2250)

    def test_boundary_conditions(self):
        self.assertEqual(cube_Sum(0), 0)
        self.assertEqual(cube_Sum(1), 8)

    def test_large_number(self):
        self.assertEqual(cube_Sum(10), 180200)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            cube_Sum(-5)
