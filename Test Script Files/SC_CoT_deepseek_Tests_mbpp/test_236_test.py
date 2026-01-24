import unittest
from mbpp_236_code import No_of_Triangle

class TestNoOfTriangle(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(No_of_Triangle(5, 2), 6)

    def test_boundary_case(self):
        self.assertEqual(No_of_Triangle(1, 1), -1)

    def test_edge_case(self):
        self.assertEqual(No_of_Triangle(10, 5), 15)
        self.assertEqual(No_of_Triangle(10, 10), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            No_of_Triangle('a', 2)
        with self.assertRaises(TypeError):
            No_of_Triangle(5, 'b')
