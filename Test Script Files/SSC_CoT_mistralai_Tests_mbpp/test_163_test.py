import unittest
from mbpp_163_code import tan, pi
from 163_code import area_polygon

class TestAreaPolygon(unittest.TestCase):

    def test_normal_input(self):
        self.assertAlmostEqual(area_polygon(3, [1, 2, 3]), 6.928203230275508)
        self.assertAlmostEqual(area_polygon(4, [1, 1, 1, 1]), 1.0)

    def test_edge_and_boundary_conditions(self):
        self.assertAlmostEqual(area_polygon(1, [1, 1]), 0.7853981633974483)
        self.assertAlmostEqual(area_polygon(2, [1, 2, 4, 8]), 24.0)
        self.assertAlmostEqual(area_polygon(0.5, [1, 1]), 0.7853981633974483)
        self.assertAlmostEqual(area_polygon(5, [1, 1, 1, 1, 1]), 2.356194490192345)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, area_polygon, 0, [1, 1])
        self.assertRaises(ValueError, area_polygon, -1, [1, 1])
        self.assertRaises(ValueError, area_polygon, 1.5, [1, 1])
        self.assertRaises(ValueError, area_polygon, 2, [1, 1, 'a'])
