import unittest
from mbpp_497_code import surfacearea_cone

class TestSurfaceAreaCone(unittest.TestCase):

    def test_surfacearea_cone(self):
        self.assertAlmostEqual(surfacearea_cone(1, 1), 4.0 * math.pi, places=2)
        self.assertAlmostEqual(surfacearea_cone(2, 3), 14.0 * math.pi, places=2)
        self.assertAlmostEqual(surfacearea_cone(0, 0), 0, places=2)
        self.assertAlmostEqual(surfacearea_cone(10, 20), 314.16 * math.pi, places=2)
