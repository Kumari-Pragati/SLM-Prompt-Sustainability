import unittest
from mbpp_449_code import check_Triangle

class TestCheckTriangle(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(check_Triangle(0,0,1,1,2,2), 'Yes')

    def test_edge_case_zero(self):
        self.assertEqual(check_Triangle(0,0,0,0,0,0), 'No')

    def test_edge_case_negative(self):
        self.assertEqual(check_Triangle(-1,-1,-2,-2,-3,-3), 'No')

    def test_edge_case_zero_sides(self):
        self.assertEqual(check_Triangle(0,0,0,0,0,0), 'No')

    def test_edge_case_zero_vertices(self):
        self.assertEqual(check_Triangle(0,0,0,0,0,0), 'No')

    def test_edge_case_negative_vertices(self):
        self.assertEqual(check_Triangle(-1,-1,-2,-2,-3,-3), 'No')

    def test_edge_case_zero_vertices_and_sides(self):
        self.assertEqual(check_Triangle(0,0,0,0,0,0), 'No')

    def test_edge_case_negative_vertices_and_sides(self):
        self.assertEqual(check_Triangle(-1,-1,-2,-2,-3,-3), 'No')

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            check_Triangle('a','b','c','d','e','f')

    def test_invalid_input_type2(self):
        with self.assertRaises(TypeError):
            check_Triangle(1,2,3,'d',4,5)

    def test_invalid_input_type3(self):
        with self.assertRaises(TypeError):
            check_Triangle(1,'b',3,4,5,6)
