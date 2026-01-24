import unittest
from mbpp_234_code import volume_cube

class TestVolumeCube(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(volume_cube(3), 27)

    def test_boundary_condition(self):
        self.assertEqual(volume_cube(0), 0)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            volume_cube(-2)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            volume_cube(2.5)
