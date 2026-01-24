import unittest
from mbpp_646_code import No_of_cubes

class TestNo_of_cubes(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(No_of_cubes(5, 2), 27)

    def test_edge_case_N_zero(self):
        with self.assertRaises(ZeroDivisionError):
            No_of_cubes(0, 2)

    def test_edge_case_K_zero(self):
        self.assertEqual(No_of_cubes(5, 0), 125)

    def test_edge_case_N_K_zero(self):
        self.assertEqual(No_of_cubes(0, 0), 0)

    def test_edge_case_N_negative(self):
        with self.assertRaises(TypeError):
            No_of_cubes(-5, 2)

    def test_edge_case_K_negative(self):
        with self.assertRaises(TypeError):
            No_of_cubes(5, -2)

    def test_edge_case_N_K_negative(self):
        with self.assertRaises(TypeError):
            No_of_cubes(-5, -2)
