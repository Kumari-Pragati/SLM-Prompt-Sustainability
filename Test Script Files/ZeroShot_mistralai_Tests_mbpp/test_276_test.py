import unittest
from mbpp_276_code import volume_cylinder

class TestVolumeCylinder(unittest.TestCase):

    def test_volume_cylinder_positive(self):
        self.assertAlmostEqual(volume_cylinder(2, 3), 15.707963267948966)
        self.assertAlmostEqual(volume_cylinder(3, 4), 113.097265625)
        self.assertAlmostEqual(volume_cylinder(1, 10), 314.1592653589793)

    def test_volume_cylinder_zero(self):
        self.assertEqual(volume_cylinder(0, 1), 0)
        self.assertEqual(volume_cylinder(1, 0), 0)

    def test_volume_cylinder_negative(self):
        self.assertAlmostEqual(volume_cylinder(-1, 2), -6.283185307179586)
        self.assertAlmostEqual(volume_cylinder(2, -1), -6.283185307179586)
