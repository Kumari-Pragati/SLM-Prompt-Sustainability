import unittest
from mbpp_234_code import volume_cube

class TestVolumeCube(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(volume_cube(3), 27)

    def test_zero(self):
        self.assertEqual(volume_cube(0), 0)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            volume_cube(-1)

    def test_float_number(self):
        self.assertAlmostEqual(volume_cube(2.5), 15.625)

    def test_large_number(self):
        self.assertEqual(volume_cube(100), 100000000)
