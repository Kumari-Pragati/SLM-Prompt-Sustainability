import unittest
from mbpp_276_code import volume_cylinder

class TestVolumeCylinder(unittest.TestCase):
    def test_positive_values(self):
        self.assertAlmostEqual(volume_cylinder(2, 3), 25.132741224606387)
        self.assertAlmostEqual(volume_cylinder(3, 4), 125.66370614406646)

    def test_zero_radius(self):
        self.assertEqual(volume_cylinder(0, 1), 0)

    def test_zero_height(self):
        self.assertEqual(volume_cylinder(1, 0), 0)

    def test_negative_values(self):
        self.assertAlmostEqual(volume_cylinder(-1, 2), -12.566370614406646)
        self.assertAlmostEqual(volume_cylinder(2, -3), -25.132741224606387)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, volume_cylinder, 'a', 1)
        self.assertRaises(TypeError, volume_cylinder, 1, 'b')
