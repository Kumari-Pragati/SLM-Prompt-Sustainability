import unittest
from mbpp_236_code import No_of_Triangle

class TestNoOfTriangle(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(No_of_Triangle(5, 2), 6)

    def test_edge_case_N_less_than_K(self):
        self.assertEqual(No_of_Triangle(3, 4), -1)

    def test_boundary_case_K_equals_N(self):
        self.assertEqual(No_of_Triangle(4, 4), 1)

    def test_boundary_case_K_equals_1(self):
        self.assertEqual(No_of_Triangle(5, 1), 10)

    def test_boundary_case_K_equals_N_minus_1(self):
        self.assertEqual(No_of_Triangle(5, 4), 1)

    def test_error_case_negative_N(self):
        with self.assertRaises(Exception):
            No_of_Triangle(-5, 2)

    def test_error_case_negative_K(self):
        with self.assertRaises(Exception):
            No_of_Triangle(5, -2)
