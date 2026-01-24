import unittest
from mbpp_276_code import volume_cylinder

class TestVolumeCylinder(unittest.TestCase):
    def test_normal_input(self):
        self.assertAlmostEqual(volume_cylinder(2, 3), 1256.63706144)

    def test_edge_and_boundary_conditions(self):
        self.assertAlmostEqual(volume_cylinder(0, 1), 0)
        self.assertAlmostEqual(volume_cylinder(1, 0), 0)
        self.assertAlmostEqual(volume_cylinder(1, 1), 3.141592653589793)
        self.assertAlmostEqual(volume_cylinder(-1, 1), 3.141592653589793)

    def test_negative_radius(self):
        self.assertRaises(ValueError, volume_cylinder, -1, 1)

    def test_negative_height(self):
        self.assertRaises(ValueError, volume_cylinder, 1, -1)
