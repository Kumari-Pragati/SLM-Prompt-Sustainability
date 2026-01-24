import unittest
from mbpp_447_code import cube_nums

class TestCubeNums(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(cube_nums([1, 2, 3]), [1, 8, 27])

    def test_edge(self):
        self.assertEqual(cube_nums([-1, 0, 1]), [-1, 0, 1])

    def test_edge2(self):
        self.assertEqual(cube_nums([1, 2, 3, 4]), [1, 8, 27, 64])

    def test_edge3(self):
        self.assertEqual(cube_nums([-1, -2, -3]), [-1, -8, -27])

    def test_edge4(self):
        self.assertEqual(cube_nums([0, 0, 0]), [0, 0, 0])

    def test_edge5(self):
        self.assertEqual(cube_nums([-1, -2, -3, -4]), [-1, -8, -27, -64])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            cube_nums('abc')
