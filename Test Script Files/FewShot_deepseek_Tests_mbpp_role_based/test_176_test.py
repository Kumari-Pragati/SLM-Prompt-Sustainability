import unittest
from mbpp_176_code import perimeter_triangle

class TestPerimeterTriangle(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(perimeter_triangle(3, 4, 5), 12)

    def test_boundary_conditions(self):
        self.assertEqual(perimeter_triangle(0, 0, 0), 0)
        self.assertEqual(perimeter_triangle(1, 1, 1), 3)

    def test_edge_conditions(self):
        self.assertEqual(perimeter_triangle(1000, 1000, 1000), 3000)
        self.assertEqual(perimeter_triangle(0.5, 0.5, 0.5), 1.5)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            perimeter_triangle("3", 4, 5)
        with self.assertRaises(TypeError):
            perimeter_triangle(3, "4", 5)
        with self.assertRaises(TypeError):
            perimeter_triangle(3, 4, "5")
        with self.assertRaises(ValueError):
            perimeter_triangle(-1, 4, 5)
        with self.assertRaises(ValueError):
            perimeter_triangle(3, -4, 5)
        with self.assertRaises(ValueError):
            perimeter_triangle(3, 4, -5)
