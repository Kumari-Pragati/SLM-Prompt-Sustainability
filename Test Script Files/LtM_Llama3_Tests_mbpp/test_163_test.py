import unittest
from mbpp_163_code import area_polygon

class TestAreaPolygon(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertAlmostEqual(area_polygon(3, 4), 6.0)
        self.assertAlmostEqual(area_polygon(4, 3), 6.0)
        self.assertAlmostEqual(area_polygon(5, 5), 12.5)

    def test_edge_cases(self):
        self.assertAlmostEqual(area_polygon(2, 2), 2.0)
        self.assertAlmostEqual(area_polygon(1, 1), 0.0)
        self.assertAlmostEqual(area_polygon(0, 0), 0.0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            area_polygon('a', 4)
        with self.assertRaises(TypeError):
            area_polygon(3, 'b')
