import unittest
from mbpp_241_code import array_3d

class TestArray3D(unittest.TestCase):

    def test_array_3d_typical(self):
        m = 2
        n = 3
        o = 4
        result = array_3d(m, n, o)
        self.assertEqual(len(result), o)
        for i in range(o):
            self.assertEqual(len(result[i]), n)
            for j in range(n):
                self.assertEqual(len(result[i][j]), m)
                self.assertEqual(result[i][j][m-1], '*')

    def test_array_3d_edge_case_m(self):
        m = 0
        n = 3
        o = 4
        with self.assertRaises(ValueError):
            array_3d(m, n, o)

    def test_array_3d_edge_case_n(self):
        m = 2
        n = 0
        o = 4
        with self.assertRaises(ValueError):
            array_3d(m, n, o)

    def test_array_3d_edge_case_o(self):
        m = 2
        n = 3
        o = 0
        with self.assertRaises(ValueError):
            array_3d(m, n, o)
