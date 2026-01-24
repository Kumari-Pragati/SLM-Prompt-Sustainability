import unittest
from mbpp_241_code import array_3d

class TestArray3D(unittest.TestCase):

    def test_empty_array(self):
        "Test creating an empty 3D array"
        result = array_3d(0, 0, 0)
        self.assertEqual(result, [])

    def test_single_dimension_array(self):
        "Test creating a 1D array"
        result = array_3d(1, 1, 1)
        self.assertEqual(result, [['*']])

    def test_two_dimension_array(self):
        "Test creating a 2D array"
        result = array_3d(2, 2, 1)
        self.assertEqual(result, [['*', '*'], ['*', '*']])

    def test_three_dimensions_array(self):
        "Test creating a 3D array"
        result = array_3d(2, 2, 2)
        self.assertEqual(result, [
            [['*', '*'], ['*', '*']],
            [['*', '*'], ['*', '*']]
        ])

    def test_negative_dimensions(self):
        "Test handling negative dimensions"
        with self.assertRaises(ValueError):
            array_3d(-1, 2, 3)

    def test_zero_dimension(self):
        "Test handling zero dimension"
        with self.assertRaises(ValueError):
            array_3d(0, 2, 3)

    def test_non_integer_dimensions(self):
        "Test handling non-integer dimensions"
        with self.assertRaises(TypeError):
            array_3d(2.5, 2, 3)
