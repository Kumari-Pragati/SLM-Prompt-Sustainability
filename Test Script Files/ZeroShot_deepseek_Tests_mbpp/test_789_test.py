import unittest
from mbpp_789_code import tan, pi
from mbpp_789_code import perimeter_polygon

class TestPerimeterPolygon(unittest.TestCase):

    def test_perimeter_polygon(self):
        self.assertEqual(perimeter_polygon(3, 4), 12)
        self.assertEqual(perimeter_polygon(5, 10), 50)
        self.assertEqual(perimeter_polygon(0, 100), 0)
        self.assertEqual(perimeter_polygon(-3, 4), -12)
        self.assertEqual(perimeter_polygon(3, -4), -12)
        self.assertEqual(perimeter_polygon(-3, -4), 12)
