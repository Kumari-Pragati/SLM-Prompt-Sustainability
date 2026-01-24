import unittest
from mbpp_731_code import lateralsurface_cone

class TestLateralSurfaceCone(unittest.TestCase):

    def test_simple_input(self):
        self.assertAlmostEqual(lateralsurface_cone(1, 2), math.pi * 3)
        self.assertAlmostEqual(lateralsurface_cone(2, 3), math.pi * 5.77350269189626)

    def test_edge_input(self):
        self.assertAlmostEqual(lateralsurface_cone(0, 1), math.pi)
        self.assertAlmostEqual(lateralsurface_cone(1, 0), math.pi)

    def test_boundary_input(self):
        self.assertAlmostEqual(lateralsurface_cone(math.inf, 1), math.pi * math.inf)
        self.assertAlmostEqual(lateralsurface_cone(1, math.inf), math.pi * math.inf)

    def test_negative_input(self):
        self.assertAlmostEqual(lateralsurface_cone(-1, 2), math.pi * math.sqrt(1 + 4))
        self.assertAlmostEqual(lateralsurface_cone(1, -2), math.pi * math.sqrt(1 + 4))
