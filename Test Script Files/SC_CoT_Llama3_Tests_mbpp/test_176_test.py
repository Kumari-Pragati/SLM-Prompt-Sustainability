import unittest
from mbpp_176_code import perimeter_triangle

class TestPerimeterTriangle(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(perimeter_triangle(3, 4, 5), 12)

    def test_edge_cases(self):
        self.assertEqual(perimeter_triangle(0, 0, 0), 0)
        self.assertEqual(perimeter_triangle(1, 1, 1), 3)
        self.assertEqual(perimeter_triangle(10, 10, 10), 30)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            perimeter_triangle('a', 4, 5)
        with self.assertRaises(TypeError):
            perimeter_triangle(3, 'b', 5)
        with self.assertRaises(TypeError):
            perimeter_triangle(3, 4, 'c')

    def test_corner_cases(self):
        self.assertEqual(perimeter_triangle(0, 5, 5), 10)
        self.assertEqual(perimeter_triangle(5, 0, 5), 10)
        self.assertEqual(perimeter_triangle(5, 5, 0), 10)
