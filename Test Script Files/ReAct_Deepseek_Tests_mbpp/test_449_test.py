import unittest
from mbpp_449_code import check_Triangle

class TestCheckTriangle(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(check_Triangle(0, 0, 1, 0, 0, 1), 'Yes')

    def test_edge_case_zero_area(self):
        self.assertEqual(check_Triangle(0, 0, 0, 0, 0, 0), 'No')

    def test_edge_case_collinear_points(self):
        self.assertEqual(check_Triangle(0, 0, 1, 1, 2, 2), 'No')

    def test_negative_coordinates(self):
        self.assertEqual(check_Triangle(-1, -1, 0, 0, 1, 1), 'Yes')

    def test_large_coordinates(self):
        self.assertEqual(check_Triangle(1000, 1000, 2000, 2000, 3000, 3000), 'Yes')

    def test_float_coordinates(self):
        self.assertEqual(check_Triangle(1.5, 1.5, 2.5, 2.5, 3.5, 3.5), 'Yes')
