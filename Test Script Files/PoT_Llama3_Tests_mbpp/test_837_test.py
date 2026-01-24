import unittest
from mbpp_837_code import cube_Sum

class TestCubeSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(cube_Sum(3), 225)

    def test_edge_case(self):
        self.assertEqual(cube_Sum(0), 0)

    def test_edge_case2(self):
        self.assertEqual(cube_Sum(1), 9)

    def test_edge_case3(self):
        self.assertEqual(cube_Sum(2), 36)

    def test_edge_case4(self):
        self.assertEqual(cube_Sum(5), 441)

    def test_edge_case5(self):
        self.assertEqual(cube_Sum(10), 3025)

    def test_edge_case6(self):
        self.assertEqual(cube_Sum(20), 14175)

    def test_edge_case7(self):
        self.assertEqual(cube_Sum(30), 43759)

    def test_edge_case8(self):
        self.assertEqual(cube_Sum(40), 103800)

    def test_edge_case9(self):
        self.assertEqual(cube_Sum(50), 225000)

    def test_edge_case10(self):
        self.assertEqual(cube_Sum(100), 13322500)
