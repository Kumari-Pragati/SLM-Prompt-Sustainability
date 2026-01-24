import unittest
from mbpp_163_code import area_polygon

class TestAreaPolygon(unittest.TestCase):

    def test_simple_case(self):
        self.assertAlmostEqual(area_polygon(3, 5), 20.80083823052924, places=5)

    def test_boundary_conditions(self):
        # Test with s = 1
        self.assertAlmostEqual(area_polygon(1, 1), 0.5, places=5)
        # Test with l = 0
        self.assertRaises(ZeroDivisionError, area_polygon, 3, 0)
        # Test with s = 0
        self.assertRaises(ZeroDivisionError, area_polygon, 0, 1)

    def test_edge_cases(self):
        # Test with negative s
        self.assertRaises(ValueError, area_polygon, -3, 5)
        # Test with negative l
        self.assertRaises(ValueError, area_polygon, 3, -5)
        # Test with non-integer s
        self.assertRaises(TypeError, area_polygon, 3.5, 5)
        # Test with non-integer l
        self.assertRaises(TypeError, area_polygon, 3, 5.5)
