import unittest
from mbpp_420_code import cube_Sum

class TestCubeSum(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(cube_Sum(1), 8)
        self.assertEqual(cube_Sum(2), 64)
        self.assertEqual(cube_Sum(3), 144)

    def test_edge_cases(self):
        self.assertEqual(cube_Sum(0), 0)
        self.assertEqual(cube_Sum(4), 288)
        self.assertEqual(cube_Sum(5), 576)

    def test_complex(self):
        self.assertEqual(cube_Sum(10), 3840)
        self.assertEqual(cube_Sum(20), 160000)
        self.assertEqual(cube_Sum(30), 466560)
