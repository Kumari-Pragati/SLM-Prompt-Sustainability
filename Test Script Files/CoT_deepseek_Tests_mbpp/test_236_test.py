import unittest
from mbpp_236_code import No_of_Triangle

class TestNoOfTriangle(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(No_of_Triangle(5, 2), 6)

    def test_edge_case(self):
        self.assertEqual(No_of_Triangle(1, 1), -1)

    def test_boundary_case(self):
        self.assertEqual(No_of_Triangle(2, 1), 1)
        self.assertEqual(No_of_Triangle(3, 1), 3)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            No_of_Triangle("5", 2)
        with self.assertRaises(TypeError):
            No_of_Triangle(5, "2")
        with self.assertRaises(TypeError):
            No_of_Triangle("5", "2")
        with self.assertRaises(ValueError):
            No_of_Triangle(-1, 2)
        with self.assertRaises(ValueError):
            No_of_Triangle(5, -2)
