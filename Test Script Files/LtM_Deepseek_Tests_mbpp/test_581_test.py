import unittest
from mbpp_581_code import surface_Area

class TestSurfaceArea(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(surface_Area(1, 2), 6)
        self.assertEqual(surface_Area(3, 4), 24)

    def test_boundary_conditions(self):
        self.assertEqual(surface_Area(0, 1), 0)
        self.assertEqual(surface_Area(1, 0), 2)
        self.assertEqual(surface_Area(0, 0), 0)

    def test_edge_cases(self):
        self.assertEqual(surface_Area(1, -1), 0)
        self.assertEqual(surface_Area(-1, 1), 0)
        self.assertEqual(surface_Area(-1, -1), 0)

    def test_complex_cases(self):
        self.assertEqual(surface_Area(5, 10), 110)
        self.assertEqual(surface_Area(10, 20), 220)
