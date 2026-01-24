import unittest
from mbpp_234_code import volume_cube

class TestVolumeCube(unittest.TestCase):

    def test_volume_cube_positive(self):
        self.assertEqual(volume_cube(1), 1)
        self.assertEqual(volume_cube(2), 8)
        self.assertEqual(volume_cube(3), 27)
        self.assertEqual(volume_cube(4), 64)
        self.assertEqual(volume_cube(5), 125)

    def test_volume_cube_zero(self):
        self.assertEqual(volume_cube(0), 0)

    def test_volume_cube_negative(self):
        self.assertRaises(ValueError, volume_cube, -1)
