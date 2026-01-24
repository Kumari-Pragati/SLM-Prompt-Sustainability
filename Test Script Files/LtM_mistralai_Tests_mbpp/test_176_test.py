import unittest
from mbpp_176_code import perimeter_triangle

class TestPerimeterTriangle(unittest.TestCase):

    def test_simple_triangle(self):
        self.assertEqual(perimeter_triangle(3, 4, 5), 12)
        self.assertEqual(perimeter_triangle(6, 8, 10), 24)

    def test_edge_cases(self):
        self.assertEqual(perimeter_triangle(0, 0, 0), 0)
        self.assertEqual(perimeter_triangle(1, 1, 1), 3)
        self.assertEqual(perimeter_triangle(1, 2, 3), 6)
        self.assertEqual(perimeter_triangle(10000, 10000, 10000), 30000)

    def test_negative_and_float_inputs(self):
        self.assertEqual(perimeter_triangle(-1, 2, 3), 6)
        self.assertEqual(perimeter_triangle(1, -2, 3), 6)
        self.assertEqual(perimeter_triangle(1, 2, -3), 6)
        self.assertEqual(perimeter_triangle(1.1, 2.2, 3.3), 6.6)
        self.assertEqual(perimeter_triangle(1, 2.2, 3.3), 6.599999999999999)
