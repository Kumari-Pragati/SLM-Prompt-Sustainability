import unittest
from mbpp_447_code import cube_nums

class TestCubeNums(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(cube_nums([1, 2, 3]), [1, 8, 27])

    def test_edge_case_zero(self):
        self.assertEqual(cube_nums([]), [])

    def test_edge_case_negative(self):
        self.assertEqual(cube_nums([-1, -2, -3]), [(-1)**3, (-2)**3, (-3)**3])

    def test_boundary_case_one(self):
        self.assertEqual(cube_nums([0]), [0])

    def test_corner_case_float(self):
        self.assertListEqual(cube_nums([2.5]), [25])
