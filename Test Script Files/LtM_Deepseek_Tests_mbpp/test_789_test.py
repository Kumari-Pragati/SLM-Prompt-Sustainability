import unittest
from mbpp_789_code import perimeter_polygon

class TestPerimeterPolygon(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(perimeter_polygon(5, 10), 50)
        self.assertEqual(perimeter_polygon(3, 7), 21)

    def test_edge_conditions(self):
        self.assertEqual(perimeter_polygon(0, 10), 0)
        self.assertEqual(perimeter_polygon(5, 0), 0)
        self.assertEqual(perimeter_polygon(0, 0), 0)

    def test_complex_cases(self):
        self.assertEqual(perimeter_polygon(1000, 10), 10000)
        self.assertEqual(perimeter_polygon(5, 1000000), 5000000)
