import unittest
from mbpp_449_code import check_Triangle

class TestCheckTriangle(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(check_Triangle(0, 0, 1, 0, 0, 1), 'Yes')

    def test_edge_case_zero_area(self):
        self.assertEqual(check_Triangle(0, 0, 0, 0, 0, 0), 'No')

    def test_boundary_case_maximum_values(self):
        self.assertEqual(check_Triangle(1000000, 1000000, 2000000, 2000000, 1500000, 1500000), 'Yes')

    def test_complex_case_negative_coordinates(self):
        self.assertEqual(check_Triangle(-1, -1, 1, 1, 0, 0), 'Yes')

    def test_invalid_input_same_coordinates(self):
        self.assertEqual(check_Triangle(1, 1, 1, 1, 1, 1), 'No')
