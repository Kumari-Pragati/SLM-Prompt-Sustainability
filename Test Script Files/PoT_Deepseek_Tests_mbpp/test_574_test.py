import unittest
from mbpp_574_code import surfacearea_cylinder

class TestSurfaceAreaCylinder(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(surfacearea_cylinder(2, 5), 62.83*2 + 62.83*10)

    def test_edge_case_zero_height(self):
        self.assertAlmostEqual(surfacearea_cylinder(3, 0), 62.83*3*2)

    def test_boundary_case_zero_radius(self):
        self.assertEqual(surfacearea_cylinder(0, 10), 0)

    def test_corner_case_negative_radius(self):
        with self.assertRaises(Exception):
            surfacearea_cylinder(-2, 5)

    def test_corner_case_negative_height(self):
        with self.assertRaises(Exception):
            surfacearea_cylinder(2, -5)
