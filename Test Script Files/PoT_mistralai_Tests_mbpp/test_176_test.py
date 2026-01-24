import unittest
from mbpp_176_code import perimeter_triangle

class TestPerimeterTriangle(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(perimeter_triangle(3, 4, 5), 12)

    def test_edge_case_zero(self):
        self.assertRaises(ValueError, perimeter_triangle, 0, 4, 5)

    def test_edge_case_negative(self):
        self.assertRaises(ValueError, perimeter_triangle, -3, 4, 5)

    def test_edge_case_one_zero(self):
        self.assertRaises(ValueError, perimeter_triangle, 3, 0, 5)

    def test_edge_case_two_zero(self):
        self.assertRaises(ValueError, perimeter_triangle, 3, 4, 0)

    def test_edge_case_sum_greater_than_1000(self):
        self.assertRaises(ValueError, perimeter_triangle, 999, 1, 1)
