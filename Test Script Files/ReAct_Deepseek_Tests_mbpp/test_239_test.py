import unittest
from mbpp_239_code import get_total_number_of_sequences

class TestGetTotalNumberOfSequences(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_total_number_of_sequences(3, 2), 5)

    def test_boundary_case_m_zero(self):
        self.assertEqual(get_total_number_of_sequences(0, 2), 0)

    def test_boundary_case_n_zero(self):
        self.assertEqual(get_total_number_of_sequences(3, 0), 0)

    def test_boundary_case_both_zero(self):
        self.assertEqual(get_total_number_of_sequences(0, 0), 0)

    def test_edge_case_m_less_than_n(self):
        self.assertEqual(get_total_number_of_sequences(2, 3), 0)

    def test_typical_case_with_large_numbers(self):
        self.assertEqual(get_total_number_of_sequences(10, 5), 1001)

    def test_error_case_negative_m(self):
        with self.assertRaises(Exception):
            get_total_number_of_sequences(-3, 2)

    def test_error_case_negative_n(self):
        with self.assertRaises(Exception):
            get_total_number_of_sequences(3, -2)
