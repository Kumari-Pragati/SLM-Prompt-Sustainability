import unittest
from mbpp_731_code import lateralsurface_cone

class TestLateralSurfaceCone(unittest.TestCase):
    def test_positive_values(self):
        self.assertAlmostEqual(lateralsurface_cone(1, 2), math.pi * 3)
        self.assertAlmostEqual(lateralsurface_cone(2, 3), math.pi * 5)
        self.assertAlmostEqual(lateralsurface_cone(3, 4), math.pi * 7)

    def test_zero_radius(self):
        self.assertAlmostEqual(lateralsurface_cone(0, 1), math.pi)

    def test_zero_height(self):
        self.assertAlmostEqual(lateralsurface_cone(1, 0), math.pi)

    def test_negative_values(self):
        self.assertAlmostEqual(lateralsurface_cone(-1, 2), math.pi * 3)
        self.assertAlmostEqual(lateralsurface_cone(1, -3), math.pi * 5)
        self.assertAlmostEqual(lateralsurface_cone(-3, -4), math.pi * 7)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, lateralsurface_cone, 0, 0)
        self.assertRaises(ValueError, lateralsurface_cone, -1, -1)
