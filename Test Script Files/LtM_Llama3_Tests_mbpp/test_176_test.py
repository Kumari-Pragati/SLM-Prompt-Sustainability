import unittest
from mbpp_176_code import perimeter_triangle

class TestPerimeterTriangle(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(perimeter_triangle(1, 2, 3), 6)
        self.assertEqual(perimeter_triangle(5, 6, 7), 18)
        self.assertEqual(perimeter_triangle(10, 20, 30), 60)

    def test_edge_cases(self):
        self.assertEqual(perimeter_triangle(0, 0, 0), 0)
        self.assertEqual(perimeter_triangle(1, 1, 1), 3)
        self.assertEqual(perimeter_triangle(10, 10, 10), 30)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            perimeter_triangle('a', 'b', 'c')
        with self.assertRaises(TypeError):
            perimeter_triangle(1, 'b', 'c')
        with self.assertRaises(TypeError):
            perimeter_triangle(1, 2, 'c')
