import unittest
from mbpp_276_code import volume_cylinder

class TestVolumeCylinder(unittest.TestCase):
    def test_positive_radius_and_height(self):
        self.assertAlmostEqual(volume_cylinder(2, 3), 25.132741224606387)

    def test_zero_radius_and_height(self):
        self.assertEqual(volume_cylinder(0, 0), 0)

    def test_negative_radius_and_positive_height(self):
        self.assertAlmostEqual(volume_cylinder(-2, 3), -25.132741224606387)

    def test_positive_radius_and_negative_height(self):
        self.assertAlmostEqual(volume_cylinder(2, -3), -25.132741224606387)

    def test_negative_radius_and_negative_height(self):
        self.assertAlmostEqual(volume_cylinder(-2, -3), 25.132741224606387)

    def test_invalid_input_radius(self):
        with self.assertRaises(ValueError):
            volume_cylinder('invalid', 3)

    def test_invalid_input_height(self):
        with self.assertRaises(ValueError):
            volume_cylinder(2, 'invalid')
