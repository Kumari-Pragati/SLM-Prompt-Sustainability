import unittest
from mbpp_731_code import lateralsurface_cone

class TestLateralSurfaceCone(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertAlmostEqual(lateralsurface_cone(1, 2), math.pi * 3)
        self.assertAlmostEqual(lateralsurface_cone(2, 3), 2 * math.pi * math.sqrt(13))

    def test_edge_and_boundary_conditions(self):
        self.assertAlmostEqual(lateralsurface_cone(0, 0), 0)
        self.assertAlmostEqual(lateralsurface_cone(1e-6, 1e6), math.pi * 1e-6 * math.sqrt(1e12))

    def test_special_cases(self):
        self.assertAlmostEqual(lateralsurface_cone(1, math.sqrt(2)), math.pi * 2)
        self.assertAlmostEqual(lateralsurface_cone(math.sqrt(2), 1), math.pi * 2)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, lateralsurface_cone, -1, 2)
        self.assertRaises(ValueError, lateralsurface_cone, 1, -2)
