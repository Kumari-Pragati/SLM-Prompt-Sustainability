import unittest
from mbpp_241_code import array_3d

class TestArray3d(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(array_3d(1, 1, 1), [[['*']]])

    def test_edge_inputs(self):
        self.assertEqual(array_3d(0, 0, 0), [])
        self.assertEqual(array_3d(1, 1, 0), [])
        self.assertEqual(array_3d(0, 1, 1), [])
        self.assertEqual(array_3d(1, 0, 1), [])

    def test_edge_inputs2(self):
        self.assertEqual(array_3d(1, 1, 1), [[['*']]])
        self.assertEqual(array_3d(1, 1, 2), [[['*']]*1]*2)
        self.assertEqual(array_3d(1, 2, 1), [[['*']]]*2)
        self.assertEqual(array_3d(2, 1, 1), [[['*']]]*2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            array_3d('a', 1, 1)
        with self.assertRaises(TypeError):
            array_3d(1, 'a', 1)
        with self.assertRaises(TypeError):
            array_3d(1, 1, 'a')
