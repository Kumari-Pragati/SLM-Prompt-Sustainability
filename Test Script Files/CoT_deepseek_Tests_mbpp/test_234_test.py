import unittest
from mbpp_234_code import volume_cube

class TestVolumeCube(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(volume_cube(3), 27)

    def test_zero(self):
        self.assertEqual(volume_cube(0), 0)

    def test_negative_integer(self):
        self.assertEqual(volume_cube(-2), -8)

    def test_positive_float(self):
        self.assertAlmostEqual(volume_cube(2.5), 15.625)

    def test_zero_float(self):
        self.assertEqual(volume_cube(0.0), 0.0)

    def test_negative_float(self):
        self.assertEqual(volume_cube(-2.5), -15.625)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            volume_cube('a')

    def test_large_number(self):
        with self.assertRaises(OverflowError):
            volume_cube(10**100)
