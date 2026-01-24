import unittest
from mbpp_581_code import surface_Area

class TestSurfaceArea(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(surface_Area(1, 1), 6)
        self.assertEqual(surface_Area(2, 2), 12)
        self.assertEqual(surface_Area(3, 3), 18)

    def test_edge_cases(self):
        self.assertEqual(surface_Area(0, 0), 0)
        self.assertEqual(surface_Area(0, 1), 2)
        self.assertEqual(surface_Area(1, 0), 2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            surface_Area('a', 1)
        with self.assertRaises(TypeError):
            surface_Area(1, 'b')
