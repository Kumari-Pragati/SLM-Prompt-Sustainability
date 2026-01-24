import unittest
from mbpp_420_code import cube_Sum

class TestCubeSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(cube_Sum(1), 8)
        self.assertEqual(cube_Sum(2), 128)
        self.assertEqual(cube_Sum(3), 1056)

    def test_boundary_cases(self):
        self.assertEqual(cube_Sum(0), 0)
        self.assertEqual(cube_Sum(10), 15360)

    def test_large_number(self):
        self.assertEqual(cube_Sum(100), 160563200)

    def test_negative_number(self):
        with self.assertRaises(AssertionError):
            cube_Sum(-1)

    def test_non_integer_input(self):
        with self.assertRaises(AssertionError):
            cube_Sum(1.5)
