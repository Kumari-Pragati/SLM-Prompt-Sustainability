import unittest
from mbpp_233_code import lateralsuface_cylinder

class TestLateralsurfaceCylinder(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(lateralsuface_cylinder(5, 10), 314.15 * 10)

    def test_edge_case_zero_radius(self):
        self.assertEqual(lateralsuface_cylinder(0, 10), 0)

    def test_boundary_case_small_radius(self):
        self.assertAlmostEqual(lateralsuface_cylinder(0.0001, 10), 0.0001 * 3.1415 * 10)

    def test_invalid_input_negative_radius(self):
        with self.assertRaises(Exception):
            lateralsuface_cylinder(-5, 10)

    def test_invalid_input_negative_height(self):
        with self.assertRaises(Exception):
            lateralsuface_cylinder(5, -10)

    def test_invalid_input_non_numeric_radius(self):
        with self.assertRaises(Exception):
            lateralsuface_cylinder('five', 10)

    def test_invalid_input_non_numeric_height(self):
        with self.assertRaises(Exception):
            lateralsuface_cylinder(5, 'ten')
