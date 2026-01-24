import unittest
from mbpp_497_code import surfacearea_cone

class TestSurfaceAreaCone(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(surfacearea_cone(3, 5), 84.77989103226922)

    def test_edge_case_zero_radius(self):
        self.assertAlmostEqual(surfacearea_cone(0, 5), 0)

    def test_edge_case_zero_height(self):
        self.assertAlmostEqual(surfacearea_cone(3, 0), 28.274333882308138)

    def test_edge_case_zero_dimensions(self):
        self.assertAlmostEqual(surfacearea_cone(0, 0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            surfacearea_cone(-3, 5)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            surfacearea_cone(3, -5)
