import unittest
from mbpp_236_code import No_of_Triangle

class TestNo_of_Triangle(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(No_of_Triangle(10, 3), 6)

    def test_edge_case_N_equal_to_K(self):
        self.assertEqual(No_of_Triangle(3, 3), 0)

    def test_edge_case_N_less_than_K(self):
        self.assertEqual(No_of_Triangle(2, 3), -1)

    def test_edge_case_N_and_K_zero(self):
        self.assertEqual(No_of_Triangle(0, 0), 0)

    def test_edge_case_N_and_K_negative(self):
        self.assertEqual(No_of_Triangle(-1, -1), -1)
