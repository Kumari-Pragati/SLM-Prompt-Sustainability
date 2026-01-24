import unittest
from mbpp_581_code import surface_Area

class TestSurfaceArea(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(surface_Area(5, 3), 62)

    def test_edge_cases(self):
        self.assertEqual(surface_Area(0, 0), 0)
        self.assertEqual(surface_Area(0, 5), 0)
        self.assertEqual(surface_Area(5, 0), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            surface_Area('a', 3)
        with self.assertRaises(TypeError):
            surface_Area(5, 'b')

    def test_boundary_conditions(self):
        self.assertEqual(surface_Area(1, 1), 4)
        self.assertEqual(surface_Area(10, 10), 420)
