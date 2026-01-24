import unittest
from mbpp_176_code import perimeter_triangle

class TestPerimeterTriangle(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(perimeter_triangle(3, 4, 5), 12)
        self.assertEqual(perimeter_triangle(5, 12, 13), 30)

    def test_edge_conditions(self):
        self.assertEqual(perimeter_triangle(0, 0, 0), 0)
        self.assertEqual(perimeter_triangle(1, 1, 1), 3)

    def test_boundary_conditions(self):
        self.assertEqual(perimeter_triangle(1, 1, 2.9999999999999996), 4)
        self.assertEqual(perimeter_triangle(1, 1, 3), 4)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            perimeter_triangle("a", 1, 1)
        with self.assertRaises(TypeError):
            perimeter_triangle(1, "b", 1)
        with self.assertRaises(TypeError):
            perimeter_triangle(1, 1, "c")
        with self.assertRaises(ValueError):
            perimeter_triangle(-1, 1, 1)
        with self.assertRaises(ValueError):
            perimeter_triangle(1, -1, 1)
        with self.assertRaises(ValueError):
            perimeter_triangle(1, 1, -1)
