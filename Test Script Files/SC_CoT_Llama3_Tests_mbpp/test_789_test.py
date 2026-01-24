import unittest
from mbpp_789_code import perimeter_polygon

class TestPerimeterPolygon(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(perimeter_polygon(5, 3), 15)

    def test_edge_cases(self):
        self.assertEqual(perimeter_polygon(0, 3), 0)
        self.assertEqual(perimeter_polygon(5, 0), 0)
        self.assertEqual(perimeter_polygon(0, 0), 0)

    def test_negative_inputs(self):
        with self.assertRaises(TypeError):
            perimeter_polygon(-5, 3)

        with self.assertRaises(TypeError):
            perimeter_polygon(5, -3)

    def test_non_numeric_inputs(self):
        with self.assertRaises(TypeError):
            perimeter_polygon('five', 3)

        with self.assertRaises(TypeError):
            perimeter_polygon(5, 'three')

    def test_mixed_inputs(self):
        with self.assertRaises(TypeError):
            perimeter_polygon(5, 'three', 4)

        with self.assertRaises(TypeError):
            perimeter_polygon('five', 3, 4)
