import unittest
from mbpp_234_code import volume_cube

class TestVolumeCube(unittest.TestCase):
    def test_volume_cube_positive(self):
        self.assertEqual(volume_cube(2), 8)

    def test_volume_cube_negative(self):
        with self.assertRaises(TypeError):
            volume_cube(-1)

    def test_volume_cube_zero(self):
        self.assertEqual(volume_cube(0), 0)

    def test_volume_cube_non_integer(self):
        with self.assertRaises(TypeError):
            volume_cube(2.5)

    def test_volume_cube_empty(self):
        with self.assertRaises(TypeError):
            volume_cube(None)
