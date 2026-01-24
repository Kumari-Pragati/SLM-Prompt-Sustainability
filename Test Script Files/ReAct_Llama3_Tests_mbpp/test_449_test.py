import unittest
from mbpp_449_code import check_Triangle

class TestCheckTriangle(unittest.TestCase):

    def test_typical_triangle(self):
        self.assertEqual(check_Triangle(0,0,3,0,0,4), 'Yes')

    def test_typical_non_triangle(self):
        self.assertEqual(check_Triangle(0,0,0,0,0,0), 'No')

    def test_edge_triangle(self):
        self.assertEqual(check_Triangle(0,0,1,0,0,1), 'Yes')

    def test_edge_non_triangle(self):
        self.assertEqual(check_Triangle(0,0,0,0,0,0), 'No')

    def test_error_case(self):
        with self.assertRaises(TypeError):
            check_Triangle('a', 'b', 'c', 'd', 'e', 'f')
