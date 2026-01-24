import unittest
from mbpp_497_code import surfacearea_cone

class TestSurfaceAreaCone(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(surfacearea_cone(3, 4), 83.2645026274, places=5)

    def test_edge_case(self):
        self.assertAlmostEqual(surfacearea_cone(0, 0), 0, places=5)

    def test_boundary_case(self):
        self.assertAlmostEqual(surfacearea_cone(1, 1), 3.14159265359, places=5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            surfacearea_cone("3", 4)
