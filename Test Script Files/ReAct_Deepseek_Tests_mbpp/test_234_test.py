import unittest
from mbpp_234_code import volume_cube

class TestVolumeCube(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(volume_cube(3), 27)

    def test_zero_length(self):
        self.assertEqual(volume_cube(0), 0)

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            volume_cube(-2)

    def test_large_number(self):
        self.assertEqual(volume_cube(1000), 1000**3)

    def test_non_integer_length(self):
        with self.assertRaises(TypeError):
            volume_cube(2.5)
