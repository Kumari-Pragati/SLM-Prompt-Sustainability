import unittest
from mbpp_241_code import array_3d

class TestArray3D(unittest.TestCase):

    def test_array_3d(self):
        m = 2
        n = 3
        o = 4
        result = array_3d(m, n, o)
        self.assertEqual(len(result), o)
        for row in result:
            self.assertEqual(len(row), n)
            for col in row:
                self.assertEqual(len(col), m)
                for item in col:
                    self.assertEqual(item, '*')

    def test_array_3d_invalid_input(self):
        with self.assertRaises(TypeError):
            array_3d('a', 2, 3)
        with self.assertRaises(TypeError):
            array_3d(2, 'b', 3)
        with self.assertRaises(TypeError):
            array_3d(2, 3, 'c')
