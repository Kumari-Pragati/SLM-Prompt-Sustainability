import unittest
from mbpp_420_code import cube_Sum

class TestCubeSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(cube_Sum(1), 8)
        self.assertEqual(cube_Sum(2), 96)
        self.assertEqual(cube_Sum(3), 288)
        self.assertEqual(cube_Sum(4), 576)
        self.assertEqual(cube_Sum(5), 960)

    def test_edge_case(self):
        self.assertEqual(cube_Sum(0), 0)
        self.assertEqual(cube_Sum(100), 16179800)

    def test_boundary_case(self):
        self.assertEqual(cube_Sum(10), 102400)
        self.assertEqual(cube_Sum(20), 68719400)
        self.assertEqual(cube_Sum(50), 1224624000)
        self.assertEqual(cube_Sum(100), 1617980000)
