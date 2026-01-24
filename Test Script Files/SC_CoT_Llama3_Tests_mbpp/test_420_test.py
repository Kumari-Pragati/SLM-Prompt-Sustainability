import unittest
from mbpp_420_code import cube_Sum

class TestCubeSum(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(cube_Sum(5), 800)

    def test_edge_case(self):
        self.assertEqual(cube_Sum(1), 0)
        self.assertEqual(cube_Sum(2), 48)

    def test_edge_case_negative(self):
        with self.assertRaises(TypeError):
            cube_Sum(-1)

    def test_edge_case_zero(self):
        self.assertEqual(cube_Sum(0), 0)

    def test_edge_case_large(self):
        self.assertEqual(cube_Sum(100), 1600000)

    def test_edge_case_negative_large(self):
        with self.assertRaises(TypeError):
            cube_Sum(-100)

    def test_edge_case_zero_large(self):
        self.assertEqual(cube_Sum(0), 0)
