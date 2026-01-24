import unittest
from mbpp_312_code import volume_cone

class TestVolumeCone(unittest.TestCase):

    def test_valid_cone(self):
        # Typical case: valid radius and height
        self.assertAlmostEqual(volume_cone(1, 2), 6.283185307179586)

    def test_zero_radius(self):
        # Edge case: zero radius
        with self.assertRaises(ValueError):
            volume_cone(0, 1)

    def test_negative_radius(self):
        # Edge case: negative radius
        with self.assertRaises(ValueError):
            volume_cone(-1, 1)

    def test_zero_height(self):
        # Edge case: zero height
        self.assertEqual(volume_cone(1, 0), 0)

    def test_negative_height(self):
        # Edge case: negative height
        with self.assertRaises(ValueError):
            volume_cone(1, -1)

    def test_invalid_input_types(self):
        # Error case: invalid input types
        with self.assertRaises(TypeError):
            volume_cone('str', 1)
