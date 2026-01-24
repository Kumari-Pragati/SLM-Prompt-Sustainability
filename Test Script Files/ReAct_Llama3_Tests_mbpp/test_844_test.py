import unittest
from mbpp_844_code import get_Number

class TestGetNumber(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_Number(10, 5), 8)

    def test_edge_case_n_equal_to_k(self):
        self.assertEqual(get_Number(5, 5), 4)

    def test_edge_case_n_equal_to_k_plus_one(self):
        self.assertRaises(IndexError, get_Number, 5, 6)

    def test_edge_case_n_equal_to_k_minus_one(self):
        self.assertRaises(IndexError, get_Number, 5, 4)

    def test_edge_case_k_greater_than_n(self):
        self.assertRaises(IndexError, get_Number, 5, 10)

    def test_edge_case_k_less_than_one(self):
        self.assertRaises(IndexError, get_Number, 5, 0)

    def test_edge_case_n_equal_to_zero(self):
        self.assertRaises(IndexError, get_Number, 0, 1)

    def test_edge_case_k_equal_to_zero(self):
        self.assertRaises(IndexError, get_Number, 5, 0)
