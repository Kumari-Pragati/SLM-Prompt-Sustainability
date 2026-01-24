import unittest
from mbpp_236_code import No_of_Triangle

class TestNo_of_Triangle(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(No_of_Triangle(10, 3), 6)

    def test_edge_case_N_eq_K(self):
        self.assertEqual(No_of_Triangle(3, 3), 0)

    def test_edge_case_N_eq_2K(self):
        self.assertEqual(No_of_Triangle(6, 3), 3)

    def test_edge_case_N_eq_K_plus_1(self):
        self.assertEqual(No_of_Triangle(4, 3), 1)

    def test_edge_case_N_eq_2K_minus_1(self):
        self.assertEqual(No_of_Triangle(5, 3), 2)

    def test_invalid_input_N_less_than_K(self):
        self.assertEqual(No_of_Triangle(3, 10), -1)

    def test_invalid_input_N_eq_K(self):
        self.assertEqual(No_of_Triangle(3, 3), -1)
