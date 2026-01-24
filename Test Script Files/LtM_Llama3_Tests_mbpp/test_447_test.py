import unittest
from mbpp_447_code import cube_nums

class TestCubeNums(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(cube_nums([1, 2, 3]), [1, 8, 27])
        self.assertEqual(cube_nums([-1, -2, -3]), [-1, -8, -27])
        self.assertEqual(cube_nums([0, 0, 0]), [0, 0, 0])

    def test_edge(self):
        self.assertEqual(cube_nums([]), [])
        self.assertEqual(cube_nums([1]), [1])
        self.assertEqual(cube_nums([1, 2, 3, 4, 5]), [1, 8, 27, 64, 125])

    def test_invalid(self):
        with self.assertRaises(TypeError):
            cube_nums('abc')
        with self.assertRaises(TypeError):
            cube_nums(None)
