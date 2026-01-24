import unittest
from mbpp_497_code import surfacearea_cone

class TestSurfaceAreaCone(unittest.TestCase):

    def test_surface_area_cone(self):
        self.assertAlmostEqual(surfacearea_cone(1,1), math.pi * 1 * (1 + math.sqrt(2)), places=5)
        self.assertAlmostEqual(surfacearea_cone(2,3), math.pi * 2 * (2 + math.sqrt(5)), places=5)
        self.assertAlmostEqual(surfacearea_cone(3,4), math.pi * 3 * (3 + math.sqrt(16)), places=5)
        self.assertAlmostEqual(surfacearea_cone(4,5), math.pi * 4 * (4 + math.sqrt(29)), places=5)
        self.assertAlmostEqual(surfacearea_cone(5,6), math.pi * 5 * (5 + math.sqrt(41)), places=5)

    def test_surface_area_cone_zero_radius(self):
        self.assertEqual(surfacearea_cone(0,1), 0)

    def test_surface_area_cone_zero_height(self):
        self.assertEqual(surfacearea_cone(1,0), 0)

    def test_surface_area_cone_zero_radius_zero_height(self):
        self.assertEqual(surfacearea_cone(0,0), 0)
