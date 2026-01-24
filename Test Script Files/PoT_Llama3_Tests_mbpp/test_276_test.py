import unittest
from mbpp_276_code import volume_cylinder

class TestVolumeCylinder(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(volume_cylinder(2, 3), 37.69949999999999)

    def test_edge_case_zero_radius(self):
        self.assertEqual(volume_cylinder(0, 3), 0)

    def test_edge_case_zero_height(self):
        self.assertEqual(volume_cylinder(2, 0), 0)

    def test_edge_case_zero_radius_and_height(self):
        self.assertEqual(volume_cylinder(0, 0), 0)

    def test_edge_case_negative_radius(self):
        with self.assertRaises(TypeError):
            volume_cylinder(-2, 3)

    def test_edge_case_negative_height(self):
        with self.assertRaises(TypeError):
            volume_cylinder(2, -3)

    def test_edge_case_negative_radius_and_height(self):
        with self.assertRaises(TypeError):
            volume_cylinder(-2, -3)
