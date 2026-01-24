import unittest
from mbpp_234_code import volume_cube

class TestVolumeCube(unittest.TestCase):
    def test_volume_cube_positive(self):
        self.assertEqual(volume_cube(2), 8)
        self.assertEqual(volume_cube(5), 125)
        self.assertEqual(volume_cube(10), 1000)

    def test_volume_cube_negative(self):
        with self.assertRaises(TypeError):
            volume_cube(-2)
        with self.assertRaises(TypeError):
            volume_cube(-5)
        with self.assertRaises(TypeError):
            volume_cube(-10)

    def test_volume_cube_zero(self):
        self.assertEqual(volume_cube(0), 0)
