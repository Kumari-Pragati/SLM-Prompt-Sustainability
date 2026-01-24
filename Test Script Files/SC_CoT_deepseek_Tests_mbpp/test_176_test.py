import unittest
from mbpp_176_code import perimeter_triangle

class TestPerimeterTriangle(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(perimeter_triangle(3, 4, 5), 12)

    def test_boundary_conditions(self):
        self.assertEqual(perimeter_triangle(0, 0, 0), 0)
        self.assertEqual(perimeter_triangle(1, 1, float('inf')), float('inf'))

    def test_edge_cases(self):
        self.assertEqual(perimeter_triangle(1, 2, 4), "Invalid input: sides do not form a triangle")
        self.assertEqual(perimeter_triangle(-1, 2, 3), "Invalid input: sides must be non-negative")
        self.assertEqual(perimeter_triangle(1, 2, 'a'), "Invalid input: sides must be numbers")

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            perimeter_triangle()
        with self.assertRaises(TypeError):
            perimeter_triangle(1)
        with self.assertRaises(TypeError):
            perimeter_triangle(1, 2)
        with self.assertRaises(TypeError):
            perimeter_triangle(1, 2, 3, 4)
