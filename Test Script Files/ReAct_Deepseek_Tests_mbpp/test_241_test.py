import unittest
from mbpp_241_code import array_3d

class TestArray3D(unittest.TestCase):

    def test_typical_case(self):
        m = 2
        n = 3
        o = 4
        result = array_3d(m, n, o)
        self.assertEqual(len(result), o)
        for i in range(o):
            self.assertEqual(len(result[i]), n)
            for j in range(n):
                self.assertEqual(len(result[i][j]), m)
                for k in range(m):
                    self.assertEqual(result[i][j][k], '*')

    def test_edge_case_zero_dimensions(self):
        m = 0
        n = 0
        o = 0
        result = array_3d(m, n, o)
        self.assertEqual(result, [])

    def test_edge_case_negative_dimensions(self):
        m = -2
        n = -3
        o = -4
        with self.assertRaises(ValueError):
            array_3d(m, n, o)

    def test_edge_case_large_dimensions(self):
        m = 1000
        n = 1000
        o = 1000
        result = array_3d(m, n, o)
        self.assertEqual(len(result), o)
        for i in range(o):
            self.assertEqual(len(result[i]), n)
            for j in range(n):
                self.assertEqual(len(result[i][j]), m)
                for k in range(m):
                    self.assertEqual(result[i][j][k], '*')
