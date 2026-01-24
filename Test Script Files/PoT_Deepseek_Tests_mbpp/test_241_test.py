import unittest
from mbpp_241_code import array_3d

class TestArray3D(unittest.TestCase):

    def test_typical_case(self):
        m, n, o = 2, 3, 4
        result = array_3d(m, n, o)
        self.assertEqual(len(result), o)
        for i in range(o):
            self.assertEqual(len(result[i]), n)
            for j in range(n):
                self.assertEqual(len(result[i][j]), m)
                for k in range(m):
                    self.assertEqual(result[i][j][k], '*')

    def test_edge_case(self):
        m, n, o = 0, 0, 0
        result = array_3d(m, n, o)
        self.assertEqual(len(result), o)
        for i in range(o):
            self.assertEqual(len(result[i]), n)
            for j in range(n):
                self.assertEqual(len(result[i][j]), m)
                self.assertEqual(len(result[i][j]), 0)

    def test_boundary_case(self):
        m, n, o = 1, 1, 1
        result = array_3d(m, n, o)
        self.assertEqual(len(result), o)
        self.assertEqual(len(result[0]), n)
        self.assertEqual(len(result[0][0]), m)
        self.assertEqual(result[0][0][0], '*')

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            array_3d(-1, 2, 3)
        with self.assertRaises(ValueError):
            array_3d(2, -2, 3)
        with self.assertRaises(ValueError):
            array_3d(2, 2, -3)
