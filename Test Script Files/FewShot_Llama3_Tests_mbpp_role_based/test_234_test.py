import unittest
from mbpp_234_code import volume_cube

class TestVolumeCube(unittest.TestCase):
    def test_positive_length(self):
        self.assertEqual(volume_cube(3), 27)

    def test_zero_length(self):
        self.assertEqual(volume_cube(0), 0)

    def test_negative_length(self):
        self.assertEqual(volume_cube(-3), 27)

    def test_non_integer_length(self):
        self.assertEqual(volume_cube(3.5), 27.375)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            volume_cube("hello")
