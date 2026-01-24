import unittest
from mbpp_646_code import No_of_cubes

class TestNoOfCubes(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(No_of_cubes(10, 5), 27000)

    def test_edge_case_N_equals_K(self):
        self.assertEqual(No_of_cubes(5, 5), 0)

    def test_boundary_case_N_greater_than_K(self):
        self.assertEqual(No_of_cubes(10, 1), 729)

    def test_boundary_case_N_less_than_K(self):
        self.assertEqual(No_of_cubes(5, 10), 0)

    def test_invalid_input_N_negative(self):
        with self.assertRaises(Exception):
            No_of_cubes(-5, 10)

    def test_invalid_input_K_negative(self):
        with self.assertRaises(Exception):
            No_of_cubes(5, -10)

    def test_invalid_input_K_greater_than_N(self):
        with self.assertRaises(Exception):
            No_of_cubes(5, 10)
