import unittest
from mbpp_239_code import get_total_number_of_sequences

class TestGetTotalNumberOfSequences(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_total_number_of_sequences(3, 2), 5)

    def test_edge_case_m_zero(self):
        self.assertEqual(get_total_number_of_sequences(0, 2), 0)

    def test_edge_case_n_zero(self):
        self.assertEqual(get_total_number_of_sequences(3, 0), 0)

    def test_edge_case_both_zero(self):
        self.assertEqual(get_total_number_of_sequences(0, 0), 0)

    def test_edge_case_j_greater_than_i(self):
        self.assertEqual(get_total_number_of_sequences(3, 4), 0)

    def test_special_case_i_equals_j(self):
        self.assertEqual(get_total_number_of_sequences(2, 2), 2)

    def test_invalid_input_negative_m(self):
        with self.assertRaises(Exception):
            get_total_number_of_sequences(-3, 2)

    def test_invalid_input_negative_n(self):
        with self.assertRaises(Exception):
            get_total_number_of_sequences(3, -2)

    def test_invalid_input_non_integer_m(self):
        with self.assertRaises(Exception):
            get_total_number_of_sequences(3.5, 2)

    def test_invalid_input_non_integer_n(self):
        with self.assertRaises(Exception):
            get_total_number_of_sequences(3, 2.5)
