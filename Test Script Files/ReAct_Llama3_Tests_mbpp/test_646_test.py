import unittest
from mbpp_646_code import No_of_cubes

class TestNo_of_cubes(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(No_of_cubes(10, 5), 125)

    def test_edge_case_N_zero(self):
        with self.assertRaises(ZeroDivisionError):
            No_of_cubes(0, 5)

    def test_edge_case_K_zero(self):
        self.assertEqual(No_of_cubes(10, 0), 1)

    def test_edge_case_N_K_equal(self):
        self.assertEqual(No_of_cubes(5, 5), 125)

    def test_edge_case_N_K_negative(self):
        with self.assertRaises(ValueError):
            No_of_cubes(-10, -5)

    def test_edge_case_N_K_zero(self):
        with self.assertRaises(ZeroDivisionError):
            No_of_cubes(0, 0)
