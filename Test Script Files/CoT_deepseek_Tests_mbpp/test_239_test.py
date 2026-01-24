import unittest
from mbpp_239_code import get_total_number_of_sequences

class TestGetTotalNumberOfSequences(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_total_number_of_sequences(3, 2), 5)

    def test_edge_case_m_zero(self):
        self.assertEqual(get_total_number_of_sequences(0, 2), 0)

    def test_edge_case_n_zero(self):
        self.assertEqual(get_total_number_of_sequences(3, 0), 0)

    def test_edge_case_m_less_than_n(self):
        self.assertEqual(get_total_number_of_sequences(2, 3), 0)

    def test_edge_case_m_and_n_one(self):
        self.assertEqual(get_total_number_of_sequences(1, 1), 1)

    def test_typical_case_large_numbers(self):
        self.assertEqual(get_total_number_of_sequences(10, 5), 101)

    def test_invalid_input_negative_m(self):
        with self.assertRaises(Exception):
            get_total_number_of_sequences(-1, 2)

    def test_invalid_input_negative_n(self):
        with self.assertRaises(Exception):
            get_total_number_of_sequences(3, -2)

    def test_invalid_input_non_integer_m(self):
        with self.assertRaises(Exception):
            get_total_number_of_sequences(1.5, 2)

    def test_invalid_input_non_integer_n(self):
        with self.assertRaises(Exception):
            get_total_number_of_sequences(3, 2.5)
