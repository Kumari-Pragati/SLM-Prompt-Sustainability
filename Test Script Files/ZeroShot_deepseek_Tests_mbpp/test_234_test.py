import unittest
from mbpp_234_code import volume_cube

class TestVolumeCube(unittest.TestCase):

    def test_volume_cube_positive_number(self):
        self.assertEqual(volume_cube(3), 27)

    def test_volume_cube_zero(self):
        self.assertEqual(volume_cube(0), 0)

    def test_volume_cube_negative_number(self):
        self.assertEqual(volume_cube(-3), -27)

    def test_volume_cube_non_integer(self):
        self.assertEqual(volume_cube(2.5), 15.625)
