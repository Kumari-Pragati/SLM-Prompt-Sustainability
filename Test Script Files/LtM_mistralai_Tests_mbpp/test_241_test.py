import unittest
from mbpp_241_code import array_3d

class TestArray3D(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(array_3d(1, 2, 3), [['*' for _ in range(2)] for _ in range(3)])
        self.assertEqual(array_3d(2, 2, 2), [['*', '*'], ['*', '*']])
        self.assertEqual(array_3d(3, 3, 3), [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']])

    def test_edge_input(self):
        self.assertEqual(array_3d(0, 0, 0), [[]])
        self.assertEqual(array_3d(0, 1, 0), [['*']])
        self.assertEqual(array_3d(1, 0, 0), [['*']])
        self.assertEqual(array_3d(0, 0, 1), [[]])

        self.assertEqual(array_3d(1, 0, 1), [['*']])
        self.assertEqual(array_3d(0, 1, 1), [['*']])

    def test_boundary_input(self):
        self.assertEqual(array_3d(1, 2, 1), [['*', '*']])
        self.assertEqual(array_3d(2, 1, 1), [['*'], ['*']])
        self.assertEqual(array_3d(1, 1, 2), [['*'], ['*']])
