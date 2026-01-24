import unittest
from mbpp_789_code import perimeter_polygon

class TestPerimeterPolygon(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(perimeter_polygon(3, 4), 12)

    def test_boundary_case(self):
        self.assertAlmostEqual(perimeter_polygon(0, 4), 0)
        self.assertAlmostEqual(perimeter_polygon(3, 0), 0)

    def test_edge_case(self):
        self.assertAlmostEqual(perimeter_polygon(1, float('inf')), float('inf'))
        self.assertAlmostEqual(perimeter_polygon(float('inf'), 1), float('inf'))

    def test_special_case(self):
        self.assertAlmostEqual(perimeter_polygon(2.5, 6), 15)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            perimeter_polygon("3", 4)
        with self.assertRaises(TypeError):
            perimeter_polygon(3, "4")
        with self.assertRaises(TypeError):
            perimeter_polygon("3", "4")
