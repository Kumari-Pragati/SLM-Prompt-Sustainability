import unittest
from mbpp_163_code import area_polygon

class TestAreaPolygon(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(area_polygon(5, 10), 125.0, places=1)

    def test_boundary_condition(self):
        self.assertAlmostEqual(area_polygon(1, 1), 0.5, places=1)

    def test_edge_condition(self):
        self.assertAlmostEqual(area_polygon(3, 1), 0.5, places=1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            area_polygon("5", 10)
        with self.assertRaises(TypeError):
            area_polygon(5, "10")
        with self.assertRaises(ValueError):
            area_polygon(0, 10)
        with self.assertRaises(ValueError):
            area_polygon(5, 0)
