import unittest
from mbpp_837_code import cube_Sum

class TestCubeSum(unittest.TestCase):

    def test_cube_Sum(self):
        self.assertEqual(cube_Sum(1), 1)
        self.assertEqual(cube_Sum(2), 94)
        self.assertEqual(cube_Sum(3), 365)
        self.assertEqual(cube_Sum(4), 882)
        self.assertEqual(cube_Sum(5), 1575)
        self.assertEqual(cube_Sum(6), 2464)
        self.assertEqual(cube_Sum(7), 3579)
        self.assertEqual(cube_Sum(8), 4930)
        self.assertEqual(cube_Sum(9), 6527)
        self.assertEqual(cube_Sum(10), 8370)
