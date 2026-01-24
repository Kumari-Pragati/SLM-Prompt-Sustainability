import unittest
from mbpp_449_code import check_Triangle

class TestCheckTriangle(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(check_Triangle(0, 0, 2, 0, 1, 2), 'Yes')

    def test_edge_case(self):
        self.assertEqual(check_Triangle(0, 0, 0, 0, 0, 0), 'No')

    def test_boundary_case(self):
        self.assertEqual(check_Triangle(1, 1, 1, 1, 1, 1), 'No')

    def test_negative_coordinates(self):
        self.assertEqual(check_Triangle(-1, -1, -2, -2, -1, -2), 'Yes')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_Triangle('a', 'b', 'c', 'd', 'e', 'f')
