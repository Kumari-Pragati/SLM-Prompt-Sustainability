import unittest
from mbpp_497_code import surfacearea_cone

class TestSurfaceAreaCone(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(surfacearea_cone(1, 2), math.pi * 5)
        self.assertEqual(surfacearea_cone(2, 3), math.pi * 13)

    def test_edge_input(self):
        self.assertAlmostEqual(surfacearea_cone(0, 1), math.pi)
        self.assertAlmostEqual(surfacearea_cone(1, 0), math.pi)

    def test_boundary_input(self):
        self.assertAlmostEqual(surfacearea_cone(1e-5, 1e-5), 2 * math.pi * 1e-5)
        self.assertAlmostEqual(surfacearea_cone(1, 1e-5), 3 * math.pi * 1e-5)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            surfacearea_cone(-1, 2)
        with self.assertRaises(ValueError):
            surfacearea_cone(1, -2)
