import unittest
from mbpp_236_code import No_of_Triangle

class TestNo_of_Triangle(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(No_of_Triangle(10, 3), 6)

    def test_edge_case_N_equal_to_K(self):
        self.assertEqual(No_of_Triangle(3, 3), 1)

    def test_edge_case_N_equal_to_2K(self):
        self.assertEqual(No_of_Triangle(6, 3), 3)

    def test_edge_case_N_equal_to_3K(self):
        self.assertEqual(No_of_Triangle(9, 3), 3)

    def test_edge_case_N_less_than_K(self):
        self.assertEqual(No_of_Triangle(5, 10), -1)

    def test_edge_case_K_greater_than_N(self):
        self.assertEqual(No_of_Triangle(5, 11), -1)

    def test_edge_case_N_equal_to_0(self):
        self.assertEqual(No_of_Triangle(0, 0), 0)

    def test_edge_case_K_equal_to_0(self):
        self.assertEqual(No_of_Triangle(10, 0), 10)

    def test_edge_case_N_equal_to_1(self):
        self.assertEqual(No_of_Triangle(1, 1), 0)

    def test_edge_case_N_equal_to_2(self):
        self.assertEqual(No_of_Triangle(2, 2), 1)

    def test_edge_case_N_equal_to_3(self):
        self.assertEqual(No_of_Triangle(3, 3), 3)

    def test_edge_case_N_equal_to_4(self):
        self.assertEqual(No_of_Triangle(4, 4), 6)

    def test_edge_case_N_equal_to_5(self):
        self.assertEqual(No_of_Triangle(5, 5), 10)
