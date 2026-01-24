import unittest
from mbpp_420_code import cube_Sum

class TestCubeSum(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(cube_Sum(3), 144)

    def test_zero(self):
        self.assertEqual(cube_Sum(0), 0)

    def test_negative_integer(self):
        self.assertEqual(cube_Sum(-3), 0)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            cube_Sum('a')

    def test_large_integer(self):
        self.assertEqual(cube_Sum(100), 3600000)
