import unittest
from mbpp_581_code import surface_Area

class TestSurfaceArea(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(surface_Area(2, 3), 16)

    def test_boundary_condition(self):
        self.assertEqual(surface_Area(0, 0), 0)

    def test_edge_condition(self):
        self.assertEqual(surface_Area(1, 1), 4)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            surface_Area("2", 3)
