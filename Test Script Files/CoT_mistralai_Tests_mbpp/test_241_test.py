import unittest
from mbpp_241_code import array_3d

class TestArray3D(unittest.TestCase):
    def test_empty_array(self):
        self.assertIsInstance(array_3d(0, 0, 0), list)
        self.assertListEqual(array_3d(0, 0, 0), [])

    def test_single_dimension(self):
        self.assertIsInstance(array_3d(1, 1, 1), list)
        self.assertListEqual(array_3d(1, 1, 1), [['*']])

    def test_two_dimensions(self):
        self.assertIsInstance(array_3d(2, 2, 1), list)
        self.assertListEqual(array_3d(2, 2, 1), [['*', '*'], ['*', '*']])

    def test_three_dimensions(self):
        self.assertIsInstance(array_3d(2, 2, 2), list)
        self.assertListEqual(array_3d(2, 2, 2), [
            [['*', '*'], ['*', '*']],
            [['*', '*'], ['*', '*']]
        ])

    def test_negative_dimensions(self):
        self.assertRaises(ValueError, array_3d, -1, 2, 3)
        self.assertRaises(ValueError, array_3d, 2, -1, 3)
        self.assertRaises(ValueError, array_3d, 2, 2, -1)

    def test_zero_dimension(self):
        self.assertRaises(ValueError, array_3d, 0, 0, 0)
