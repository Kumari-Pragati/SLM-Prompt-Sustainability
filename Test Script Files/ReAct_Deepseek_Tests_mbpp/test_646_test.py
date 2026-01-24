import unittest
from mbpp_646_code import No_of_cubes

class TestNoOfCubes(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(No_of_cubes(10, 5), 27000)

    def test_boundary_case_N_equals_K(self):
        self.assertEqual(No_of_cubes(5, 5), 0)

    def test_boundary_case_N_less_than_K(self):
        with self.assertRaises(ValueError):
            No_of_cubes(3, 4)

    def test_negative_values(self):
        self.assertEqual(No_of_cubes(-10, -5), -27000)

    def test_zero_values(self):
        self.assertEqual(No_of_cubes(0, 0), 0)

    def test_large_numbers(self):
        self.assertEqual(No_of_cubes(1000, 500), 500**3)
