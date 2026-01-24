import unittest
from mbpp_581_code import surface_Area

class TestSurfaceArea(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(surface_Area(2, 3), 18)
        self.assertEqual(surface_Area(4, 5), 28)

    def test_edge_cases(self):
        self.assertEqual(surface_Area(0, 0), 0)
        self.assertEqual(surface_Area(0, 10), 20)
        self.assertEqual(surface_Area(10, 0), 20)

    def test_negative_inputs(self):
        with self.assertRaises(TypeError):
            surface_Area(-2, 3)
        with self.assertRaises(TypeError):
            surface_Area(2, -3)

    def test_non_numeric_inputs(self):
        with self.assertRaises(TypeError):
            surface_Area('a', 3)
        with self.assertRaises(TypeError):
            surface_Area(2, 'b')

    def test_zero_inputs(self):
        self.assertEqual(surface_Area(0, 0), 0)
        self.assertEqual(surface_Area(0, 10), 20)
        self.assertEqual(surface_Area(10, 0), 20)
