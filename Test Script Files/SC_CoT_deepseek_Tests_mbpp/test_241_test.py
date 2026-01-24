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

    def test_edge_cases(self):
        self.assertEqual(array_3d(0, 0, 0), [])
        self.assertEqual(array_3d(1, 1, 1), [ [ [ '*' ] ] ])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            array_3d('2', 3, 4)
        with self.assertRaises(TypeError):
            array_3d(2, '3', 4)
        with self.assertRaises(TypeError):
            array_3d(2, 3, '4')
        with self.assertRaises(ValueError):
            array_3d(-1, 3, 4)
        with self.assertRaises(ValueError):
            array_3d(2, -3, 4)
        with self.assertRaises(ValueError):
            array_3d(2, 3, -4)
