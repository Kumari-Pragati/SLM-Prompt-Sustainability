import unittest
from mbpp_420_code import cube_Sum

class TestCubeSum(unittest.TestCase):

    def test_cube_Sum(self):
        self.assertEqual(cube_Sum(1), 8)
        self.assertEqual(cube_Sum(2), 144)
        self.assertEqual(cube_Sum(3), 1040)
        self.assertEqual(cube_Sum(4), 4000)
        self.assertEqual(cube_Sum(5), 8000)
        self.assertEqual(cube_Sum(6), 11200)
        self.assertEqual(cube_Sum(7), 12800)
        self.assertEqual(cube_Sum(8), 12800)
        self.assertEqual(cube_Sum(9), 10400)
        self.assertEqual(cube_Sum(10), 6400)
