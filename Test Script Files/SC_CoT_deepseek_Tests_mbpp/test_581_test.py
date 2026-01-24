import unittest
from mbpp_581_code import surface_Area

class TestSurfaceArea(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertAlmostEqual(surface_Area(3, 4), 26.0)

    def test_edge_case(self):
        self.assertAlmostEqual(surface_Area(0, 5), 0.0)
        self.assertAlmostEqual(surface_Area(5, 0), 25.0)
        self.assertAlmostEqual(surface_Area(0, 0), 0.0)

    def test_corner_case(self):
        self.assertAlmostEqual(surface_Area(-3, 4), -14.0)
        self.assertAlmostEqual(surface_Area(3, -4), 14.0)
        self.assertAlmostEqual(surface_Area(-3, -4), -14.0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            surface_Area("3", 4)
        with self.assertRaises(TypeError):
            surface_Area(3, "4")
        with self.assertRaises(TypeError):
            surface_Area("3", "4")
