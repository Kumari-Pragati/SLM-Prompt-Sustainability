import unittest
from mbpp_837_code import cube_Sum

class TestCubeSum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(cube_Sum(1), 9)
        self.assertEqual(cube_Sum(2), 81)
        self.assertEqual(cube_Sum(3), 225)

    def test_edge(self):
        self.assertEqual(cube_Sum(0), 0)
        self.assertEqual(cube_Sum(1), 9)
        self.assertEqual(cube_Sum(-1), 0)

    def test_edge2(self):
        self.assertEqual(cube_Sum(10), 3025)
        self.assertEqual(cube_Sum(-10), 0)

    def test_edge3(self):
        self.assertEqual(cube_Sum(100), 10010001)
        self.assertEqual(cube_Sum(-100), 0)

    def test_edge4(self):
        self.assertEqual(cube_Sum(1000), 1000001001)
        self.assertEqual(cube_Sum(-1000), 0)
