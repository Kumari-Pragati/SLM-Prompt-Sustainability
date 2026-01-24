import unittest
from mbpp_163_code import area_polygon

class TestAreaPolygon(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertAlmostEqual(area_polygon(3, 4), 6.0, places=5)

    def test_edge_cases(self):
        self.assertAlmostEqual(area_polygon(1, 4), 4.0, places=5)
        self.assertAlmostEqual(area_polygon(2, 4), 8.0, places=5)
        self.assertAlmostEqual(area_polygon(3, 4), 12.0, places=5)

    def test_invalid_inputs(self):
        with self.assertRaises(ZeroDivisionError):
            area_polygon(0, 4)
        with self.assertRaises(ZeroDivisionError):
            area_polygon(3, 0)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(area_polygon(4, 4), 8.0, places=5)
        self.assertAlmostEqual(area_polygon(5, 4), 10.0, places=5)
