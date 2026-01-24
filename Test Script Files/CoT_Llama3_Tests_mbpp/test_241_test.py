import unittest
from mbpp_241_code import array_3d

class TestArray3D(unittest.TestCase):
    def test_array_3d_default(self):
        result = array_3d(2, 3, 4)
        self.assertEqual(len(result), 4)
        self.assertEqual(len(result[0]), 3)
        self.assertEqual(len(result[0][0]), 2)

    def test_array_3d_non_default(self):
        result = array_3d(5, 6, 7)
        self.assertEqual(len(result), 7)
        self.assertEqual(len(result[0]), 6)
        self.assertEqual(len(result[0][0]), 5)

    def test_array_3d_zero(self):
        result = array_3d(0, 0, 0)
        self.assertEqual(result, [])

    def test_array_3d_negative(self):
        with self.assertRaises(TypeError):
            array_3d(-1, 2, 3)

    def test_array_3d_non_integer(self):
        with self.assertRaises(TypeError):
            array_3d('a', 2, 3)
