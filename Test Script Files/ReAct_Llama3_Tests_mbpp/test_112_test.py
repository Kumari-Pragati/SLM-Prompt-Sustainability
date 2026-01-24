import unittest
from mbpp_112_code import perimeter

class TestPerimeter(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(perimeter(10, 5), 30)

    def test_edge_case_diameter_zero(self):
        self.assertEqual(perimeter(0, 5), 10)

    def test_edge_case_height_zero(self):
        self.assertEqual(perimeter(10, 0), 20)

    def test_edge_case_diameter_and_height_zero(self):
        self.assertEqual(perimeter(0, 0), 0)

    def test_edge_case_negative_diameter(self):
        with self.assertRaises(TypeError):
            perimeter(-10, 5)

    def test_edge_case_negative_height(self):
        with self.assertRaises(TypeError):
            perimeter(10, -5)

    def test_edge_case_non_numeric_diameter(self):
        with self.assertRaises(TypeError):
            perimeter('ten', 5)

    def test_edge_case_non_numeric_height(self):
        with self.assertRaises(TypeError):
            perimeter(10, 'five')
