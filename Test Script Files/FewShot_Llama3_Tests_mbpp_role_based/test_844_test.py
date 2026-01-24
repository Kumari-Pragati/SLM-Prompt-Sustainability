import unittest
from mbpp_844_code import get_Number

class TestGetNumber(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(get_Number(10, 5), 10)

    def test_edge_case_n_equal_to_k(self):
        self.assertEqual(get_Number(5, 5), 5)

    def test_edge_case_n_greater_than_k(self):
        self.assertEqual(get_Number(10, 1), 1)

    def test_edge_case_n_equal_to_zero(self):
        with self.assertRaises(IndexError):
            get_Number(0, 1)

    def test_edge_case_k_greater_than_n(self):
        with self.assertRaises(IndexError):
            get_Number(10, 11)

    def test_edge_case_n_and_k_equal_to_zero(self):
        with self.assertRaises(IndexError):
            get_Number(0, 0)
