import unittest
from mbpp_574_code import surfacearea_cylinder

class TestSurfaceAreaCylinder(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(surfacearea_cylinder(5, 10), 3.1415 * (5 * 5 + 5 * 10), places=5)

    def test_edge_case_zero_radius(self):
        self.assertAlmostEqual(surfacearea_cylinder(0, 10), 0, places=5)

    def test_edge_case_zero_height(self):
        self.assertAlmostEqual(surfacearea_cylinder(5, 0), 2 * 3.1415 * 5 * 5, places=5)

    def test_edge_case_zero_radius_and_height(self):
        self.assertAlmostEqual(surfacearea_cylinder(0, 0), 0, places=5)

    def test_edge_case_negative_radius(self):
        with self.assertRaises(TypeError):
            surfacearea_cylinder(-5, 10)

    def test_edge_case_negative_height(self):
        with self.assertRaises(TypeError):
            surfacearea_cylinder(5, -10)

    def test_edge_case_non_numeric_radius(self):
        with self.assertRaises(TypeError):
            surfacearea_cylinder('five', 10)

    def test_edge_case_non_numeric_height(self):
        with self.assertRaises(TypeError):
            surfacearea_cylinder(5, 'ten')
