import unittest
from mbpp_233_code import lateralsuface_cylinder

class TestLateralSurfaceCylinder(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(lateralsuface_cylinder(1, 2), 12.56636807138678)

    def test_edge_case_zero_radius(self):
        self.assertEqual(lateralsuface_cylinder(0, 1), 0)

    def test_edge_case_zero_height(self):
        self.assertEqual(lateralsuface_cylinder(1, 0), 0)

    def test_corner_case_negative_radius(self):
        self.assertEqual(lateralsuface_cylinder(-1, 1), -2.094395102393199)

    def test_corner_case_negative_height(self):
        self.assertEqual(lateralsuface_cylinder(1, -1), -2.094395102393199)
