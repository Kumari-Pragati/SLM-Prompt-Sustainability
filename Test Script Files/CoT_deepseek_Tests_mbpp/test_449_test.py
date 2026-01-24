import unittest
from mbpp_449_code import check_Triangle

class TestCheckTriangle(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(check_Triangle(0, 0, 1, 0, 0, 1), 'Yes')

    def test_edge_case(self):
        self.assertEqual(check_Triangle(0, 0, 0, 0, 0, 0), 'No')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_Triangle('a', 'b', 'c', 'd', 'e', 'f')

    def test_negative_coordinates(self):
        self.assertEqual(check_Triangle(-1, -1, 1, -1, 0, 1), 'Yes')

    def test_large_coordinates(self):
        self.assertEqual(check_Triangle(1000000, 1000000, 2000000, 1000000, 1500000, 1500000), 'Yes')
