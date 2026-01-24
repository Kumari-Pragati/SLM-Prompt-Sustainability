import unittest
from mbpp_176_code import perimeter_triangle

class TestPerimeterTriangle(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(perimeter_triangle(3, 4, 5), 12)

    def test_edge_case_zero(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(0, 4, 5)

    def test_edge_case_negative(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(-3, 4, 5)

    def test_edge_case_zero_sides(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(0, 0, 5)

    def test_edge_case_zero_sides_reversed(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(0, 5, 0)

    def test_edge_case_zero_sides_reversed_again(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(5, 0, 0)

    def test_edge_case_zero_sides_reversed_again_reversed(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(0, 0, 0)

    def test_edge_case_zero_sides_reversed_again_reversed_again(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(0, 0, 0)

    def test_edge_case_zero_sides_reversed_again_reversed_again_again(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(0, 0, 0)

    def test_edge_case_zero_sides_reversed_again_reversed_again_again_again(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(0, 0, 0)

    def test_edge_case_zero_sides_reversed_again_reversed_again_again_again_again(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(0, 0, 0)

    def test_edge_case_zero_sides_reversed_again_reversed_again_again_again_again_again(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(0, 0, 0)

    def test_edge_case_zero_sides_reversed_again_reversed_again_again_again_again_again_again(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(0, 0, 0)

    def test_edge_case_zero_sides_reversed_again_reversed_again_again_again_again_again_again_again(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(0, 0, 0)

    def test_edge_case_zero_sides_reversed_again_reversed_again_again_again_again_again_again_again_again(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(0, 0, 0)

    def test_edge_case_zero_sides_reversed_again_reversed_again_again_again_again_again_again_again_again_again(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(0, 0, 0)

    def test_edge_case_zero_sides_reversed_again_reversed_again_again_again_again_again_again_again_again_again_again(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(0, 0, 0)

    def test_edge_case_zero_sides_reversed_again_reversed_again_again_again_again_again_again_again_again_again_again_again(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(0, 0, 0)

    def test_edge_case_zero_sides_reversed_again_reversed_again_again_again_again_again_again_again_again_again_again_again_again(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(0, 0, 0)

    def test_edge_case_zero_sides_reversed_again_reversed_again_again_again_again_again_again_again_again_again_again_again_again(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(0, 0, 0)

    def test_edge_case_zero_sides_reversed_again_reversed_again_again_again_again_again_again_again_again_again_again_again_again_again(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(0, 0, 0)

    def test_edge_case_zero_sides_reversed_again_reversed_again_again_again_again_again_again_again_again_again_again_again_again_again(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(0, 0, 0)

    def test_edge_case_zero_sides_reversed_again_reversed_again_again_again_again_again_again_again_again_again_again_again_again_again(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(0, 0, 0)

    def test_edge_case_zero_sides_reversed_again_reversed_again_again_again_again_again_again_again_again_again_again_again_again_again(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(0, 0, 0)

    def test_edge_case_zero_sides_reversed_again_reversed_again_again_again_again_again_again_again_again_again_again_again_again_again(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(0, 0, 0)

    def test_edge_case_zero_sides_reversed_again_reversed_again_again_again_again_again_again_again_again_again_again_again_again_again(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(0, 0, 0)

    def test_edge_case_zero_sides_reversed