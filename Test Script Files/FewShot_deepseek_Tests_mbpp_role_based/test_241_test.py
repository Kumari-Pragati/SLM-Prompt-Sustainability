import unittest
from mbpp_241_code import array_3d

class TestArray3D(unittest.TestCase):
    def test_typical_use_case(self):
        result = array_3d(2, 3, 4)
        self.assertEqual(len(result), 4)
        for i in range(4):
            self.assertEqual(len(result[i]), 3)
            for j in range(3):
                self.assertEqual(len(result[i][j]), 2)
                for k in range(2):
                    self.assertEqual(result[i][j][k], '*')

    def test_edge_conditions(self):
        self.assertEqual(array_3d(0, 0, 0), [])
        self.assertEqual(array_3d(1, 1, 1), [ [ [ '*' ] ] ])

    def test_boundary_conditions(self):
        result = array_3d(1000, 1000, 1000)
        self.assertEqual(len(result), 1000)
        for i in range(1000):
            self.assertEqual(len(result[i]), 1000)
            for j in range(1000):
                self.assertEqual(len(result[i][j]), 1000)
                for k in range(1000):
                    self.assertEqual(result[i][j][k], '*')

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            array_3d('a', 2, 3)
        with self.assertRaises(TypeError):
            array_3d(2, 'b', 3)
        with self.assertRaises(TypeError):
            array_3d(2, 3, 'c')
