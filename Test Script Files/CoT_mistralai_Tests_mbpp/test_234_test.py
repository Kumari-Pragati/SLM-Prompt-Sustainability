import unittest
from mbpp_234_code import volume_cube

class TestVolumeCube(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(volume_cube(3), 27)
        self.assertEqual(volume_cube(5), 125)

    def test_zero(self):
        self.assertEqual(volume_cube(0), 0)

    def test_negative_number(self):
        self.assertEqual(volume_cube(-1), -1)

    def test_float(self):
        self.assertAlmostEqual(volume_cube(2.5), 15.625)

    def test_string(self):
        with self.assertRaises(ValueError):
            volume_cube('str')

    def test_list(self):
        with self.assertRaises(TypeError):
            volume_cube([1, 2, 3])
