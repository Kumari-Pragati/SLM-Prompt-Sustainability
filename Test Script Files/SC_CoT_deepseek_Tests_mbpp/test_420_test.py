import unittest
from mbpp_420_code import cube_Sum

class TestCubeSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(cube_Sum(1), 8)
        self.assertEqual(cube_Sum(2), 216)
        self.assertEqual(cube_Sum(3), 10404)

    def test_boundary_case(self):
        self.assertEqual(cube_Sum(0), 0)

    def test_edge_case(self):
        self.assertEqual(cube_Sum(-1), 0)
        self.assertEqual(cube_Sum(4), 27556344)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            cube_Sum("test")
        with self.assertRaises(TypeError):
            cube_Sum(None)
        with self.assertRaises(TypeError):
            cube_Sum([])
