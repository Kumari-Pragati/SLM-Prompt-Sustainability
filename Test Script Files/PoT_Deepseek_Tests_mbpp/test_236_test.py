import unittest
from mbpp_236_code import No_of_Triangle

class TestNoOfTriangle(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(No_of_Triangle(5, 2), 6)
        self.assertEqual(No_of_Triangle(10, 3), 14)

    def test_edge_cases(self):
        self.assertEqual(No_of_Triangle(1, 1), -1)
        self.assertEqual(No_of_Triangle(0, 0), -1)
        self.assertEqual(No_of_Triangle(2, 3), -1)

    def test_boundary_cases(self):
        self.assertEqual(No_of_Triangle(2, 1), 1)
        self.assertEqual(No_of_Triangle(3, 1), 3)
        self.assertEqual(No_of_Triangle(4, 2), 4)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            No_of_Triangle("5", 2)
        with self.assertRaises(TypeError):
            No_of_Triangle(5, "2")
        with self.assertRaises(TypeError):
            No_of_Triangle("5", "2")
