import unittest
from mbpp_497_code import surfacearea_cone

class TestSurfaceAreaCone(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(surfacearea_cone(3, 5), 84.77989278923265)

    def test_zero_radius(self):
        self.assertAlmostEqual(surfacearea_cone(0, 5), 0)

    def test_zero_height(self):
        self.assertAlmostEqual(surfacearea_cone(3, 0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            surfacearea_cone(-3, 5)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            surfacearea_cone(3, -5)

    def test_large_radius_and_height(self):
        self.assertAlmostEqual(surfacearea_cone(1000, 1000), 3141592.653589793)
