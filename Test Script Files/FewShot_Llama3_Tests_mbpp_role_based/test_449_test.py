import unittest
from mbpp_449_code import check_Triangle

class TestCheckTriangle(unittest.TestCase):
    def test_valid_triangle(self):
        self.assertEqual(check_Triangle(0,0,0,0,0,0), 'Yes')

    def test_non_valid_triangle(self):
        self.assertEqual(check_Triangle(0,0,0,0,0,1), 'No')

    def test_edge_case_triangle(self):
        self.assertEqual(check_Triangle(0,0,0,0,0,0.5), 'Yes')

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            check_Triangle('a',0,0,0,0,0)

    def test_invalid_input_value(self):
        with self.assertRaises(ValueError):
            check_Triangle(0,0,0,0,0,0.5)
