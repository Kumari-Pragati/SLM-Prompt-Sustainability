import unittest
from mbpp_276_code import volume_cylinder

class TestVolumeCylinder(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(volume_cylinder(2, 3), 25.13274122471765)

    def test_edge_case_zero_radius(self):
        self.assertEqual(volume_cylinder(0, 1), 0)

    def test_edge_case_zero_height(self):
        self.assertEqual(volume_cylinder(1, 0), 0)

    def test_boundary_case_small_radius(self):
        self.assertEqual(volume_cylinder(0.01, 1), 0.0003141592653589793)

    def test_boundary_case_small_height(self):
        self.assertEqual(volume_cylinder(1, 0.01), 0.03141592653589793)
