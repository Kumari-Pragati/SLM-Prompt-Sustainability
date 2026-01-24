import unittest
from mbpp_581_code import surface_Area

class TestSurfaceArea(unittest.TestCase):
    def test_normal_inputs(self):
        self.assertEqual(surface_Area(2, 3), 20)
        self.assertEqual(surface_Area(4, 5), 50)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(surface_Area(0, 5), 0)
        self.assertEqual(surface_Area(5, 0), 0)
        self.assertEqual(surface_Area(1, 1), 8)
        self.assertEqual(surface_Area(0.5, 1), 3.5)

    def test_negative_inputs(self):
        self.assertRaises(ValueError, surface_Area, -1, 2)
        self.assertRaises(ValueError, surface_Area, 2, -1)
