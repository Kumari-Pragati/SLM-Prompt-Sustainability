import unittest
from mbpp_581_code import surface_Area

class TestSurfaceArea(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(surface_Area(2, 3), 20)
        self.assertEqual(surface_Area(4, 5), 60)

    def test_edge_cases(self):
        self.assertEqual(surface_Area(0, 1), 2)
        self.assertEqual(surface_Area(1, 0), 1)
        self.assertEqual(surface_Area(1, 0), 1)
        self.assertEqual(surface_Area(1, 1), 6)

    def test_negative_and_zero_inputs(self):
        self.assertEqual(surface_Area(-1, 2), None)
        self.assertEqual(surface_Area(0, -1), None)
        self.assertEqual(surface_Area(0, 0), 0)
