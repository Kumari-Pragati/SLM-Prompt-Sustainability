import unittest
from mbpp_176_code import perimeter_triangle

class TestPerimeterTriangle(unittest.TestCase):
    def test_normal_inputs(self):
        self.assertEqual(perimeter_triangle(3, 4, 5), 12)
        self.assertEqual(perimeter_triangle(6, 8, 10), 24)

    def test_edge_cases(self):
        self.assertEqual(perimeter_triangle(0, 0, 0), 0)
        self.assertEqual(perimeter_triangle(1, 1, 1), 3)
        self.assertEqual(perimeter_triangle(1000000, 1000000, 1000000), 3000000)

    def test_negative_inputs(self):
        self.assertRaises(ValueError, perimeter_triangle, -1, 2, 3)
        self.assertRaises(ValueError, perimeter_triangle, 1, -2, 3)
        self.assertRaises(ValueError, perimeter_triangle, 1, 2, -3)

    def test_float_inputs(self):
        self.assertAlmostEqual(perimeter_triangle(3.1, 4.2, 5.3), 12.6)
        self.assertRaises(TypeError, perimeter_triangle, 3.1, 4, 5)
        self.assertRaises(TypeError, perimeter_triangle, 3, 4.2, 5.3)
