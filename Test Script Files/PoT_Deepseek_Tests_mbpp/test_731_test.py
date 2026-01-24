import unittest
from mbpp_731_code import lateralsurface_cone

class TestLatersurfaceCone(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(lateralsurface_cone(5, 12), 261.7993877991494)

    def test_edge_case_zero_radius(self):
        self.assertEqual(lateralsurface_cone(0, 10), 0)

    def test_edge_case_zero_height(self):
        self.assertEqual(lateralsurface_cone(5, 0), 0)

    def test_boundary_case_radius_one(self):
        self.assertAlmostEqual(lateralsurface_cone(1, 10), 31.41592653589793)

    def test_boundary_case_height_one(self):
        self.assertAlmostEqual(lateralsurface_cone(5, 1), 31.41592653589793)

    def test_corner_case_negative_radius(self):
        with self.assertRaises(ValueError):
            lateralsurface_cone(-5, 10)

    def test_corner_case_negative_height(self):
        with self.assertRaises(ValueError):
            lateralsurface_cone(5, -10)
