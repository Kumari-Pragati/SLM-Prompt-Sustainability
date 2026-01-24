import unittest
from mbpp_276_code import volume_cylinder

class TestVolumeCylinder(unittest.TestCase):

    def test_positive_values(self):
        """Test volume calculation with positive values"""
        self.assertAlmostEqual(volume_cylinder(2, 3), 15.707963267948966)
        self.assertAlmostEqual(volume_cylinder(1, 1), 3.141592653589793)

    def test_zero_radius(self):
        """Test volume calculation with zero radius"""
        with self.assertRaises(ValueError):
            volume_cylinder(0, 1)

    def test_negative_radius(self):
        """Test volume calculation with negative radius"""
        with self.assertRaises(ValueError):
            volume_cylinder(-1, 1)

    def test_negative_height(self):
        """Test volume calculation with negative height"""
        with self.assertRaises(ValueError):
            volume_cylinder(1, -1)

    def test_zero_height(self):
        """Test volume calculation with zero height"""
        self.assertEqual(volume_cylinder(1, 0), 0)
