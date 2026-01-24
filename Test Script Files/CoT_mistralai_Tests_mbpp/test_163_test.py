import unittest
from mbpp_163_code import tan, pi
from sixteen_thirty_three_code import area_polygon

class TestAreaPolygon(unittest.TestCase):
    def test_valid_inputs(self):
        self.assertAlmostEqual(area_polygon(3, 4), 6.928203230275509)
        self.assertAlmostEqual(area_polygon(4, 3), 12.566370614359173)
        self.assertAlmostEqual(area_polygon(5, 2), 25.0)

    def test_edge_cases(self):
        self.assertAlmostEqual(area_polygon(2, 1), 2.0000000000000004)
        self.assertAlmostEqual(area_polygon(1, 2), 1.5707963267948966)
        self.assertAlmostEqual(area_polygon(0.5, 1), 0.7853981633974483)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, area_polygon, 0, 1)
        self.assertRaises(ValueError, area_polygon, -1, 1)
        self.assertRaises(ValueError, area_polygon, 1, 0)
