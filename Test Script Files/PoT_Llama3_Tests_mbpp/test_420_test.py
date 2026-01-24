import unittest
from mbpp_420_code import cube_Sum

class TestCubeSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(cube_Sum(5), 980)

    def test_edge_case(self):
        self.assertEqual(cube_Sum(0), 0)
        self.assertEqual(cube_Sum(1), 8)

    def test_edge_case_negative(self):
        with self.assertRaises(TypeError):
            cube_Sum(-1)

    def test_edge_case_non_integer(self):
        with self.assertRaises(TypeError):
            cube_Sum('a')

    def test_edge_case_large(self):
        self.assertEqual(cube_Sum(100), 9800000)

    def test_edge_case_zero(self):
        self.assertEqual(cube_Sum(0), 0)
