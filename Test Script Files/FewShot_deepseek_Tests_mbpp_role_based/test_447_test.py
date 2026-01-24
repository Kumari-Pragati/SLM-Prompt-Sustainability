import unittest
from mbpp_447_code import cube_nums

class TestCubeNums(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(cube_nums([1, 2, 3]), [1, 8, 27])

    def test_edge_condition(self):
        self.assertEqual(cube_nums([0]), [0])

    def test_boundary_condition(self):
        self.assertEqual(cube_nums([-1, 1]), [-1, 1])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            cube_nums("1, 2, 3")
