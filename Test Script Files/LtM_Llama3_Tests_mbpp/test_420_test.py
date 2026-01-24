import unittest
from mbpp_420_code import cube_Sum

class TestCubeSum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(cube_Sum(1), 8)
        self.assertEqual(cube_Sum(2), 64)
        self.assertEqual(cube_Sum(3), 216)

    def test_edge(self):
        self.assertEqual(cube_Sum(0), 0)
        self.assertEqual(cube_Sum(1), 8)
        self.assertEqual(cube_Sum(4), 576)

    def test_edge_negative(self):
        self.assertEqual(cube_Sum(-1), 0)
        self.assertEqual(cube_Sum(-2), 0)
        self.assertEqual(cube_Sum(-3), 0)

    def test_edge_zero(self):
        self.assertEqual(cube_Sum(0), 0)

    def test_edge_max(self):
        self.assertEqual(cube_Sum(1000), 1000000000)
