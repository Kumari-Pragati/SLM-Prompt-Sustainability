import unittest
from mbpp_236_code import No_of_Triangle

class TestNo_of_Triangle(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(No_of_Triangle(5, 3), 6)
        self.assertEqual(No_of_Triangle(10, 5), 35)

    def test_edge_cases_N_K(self):
        self.assertEqual(No_of_Triangle(0, 0), -1)
        self.assertEqual(No_of_Triangle(1, 0), -1)
        self.assertEqual(No_of_Triangle(0, 1), -1)

    def test_edge_cases_N(self):
        self.assertEqual(No_of_Triangle(1, 1), 1)
        self.assertEqual(No_of_Triangle(2, 1), 1)

    def test_edge_cases_K(self):
        self.assertEqual(No_of_Triangle(5, 0), -1)
        self.assertEqual(No_of_Triangle(5, 1), 5)
        self.assertEqual(No_of_Triangle(5, 2), 0)

    def test_negative_K(self):
        self.assertEqual(No_of_Triangle(5, -2), -1)
