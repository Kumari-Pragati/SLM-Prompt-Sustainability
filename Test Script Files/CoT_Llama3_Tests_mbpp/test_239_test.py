import unittest
from mbpp_239_code import get_total_number_of_sequences

class TestGetTotalNumberOfSequences(unittest.TestCase):
    def test_zero_input(self):
        self.assertEqual(get_total_number_of_sequences(0, 0), 0)

    def test_single_digit_input(self):
        self.assertEqual(get_total_number_of_sequences(1, 1), 1)

    def test_two_digit_input(self):
        self.assertEqual(get_total_number_of_sequences(2, 2), 2)

    def test_edge_case_m_zero_n_one(self):
        self.assertEqual(get_total_number_of_sequences(0, 1), 0)

    def test_edge_case_m_one_n_zero(self):
        self.assertEqual(get_total_number_of_sequences(1, 0), 0)

    def test_edge_case_m_one_n_one(self):
        self.assertEqual(get_total_number_of_sequences(1, 1), 1)

    def test_edge_case_m_zero_n_zero(self):
        self.assertEqual(get_total_number_of_sequences(0, 0), 0)

    def test_invalid_input_m_negative_n_positive(self):
        with self.assertRaises(ValueError):
            get_total_number_of_sequences(-1, 2)

    def test_invalid_input_m_positive_n_negative(self):
        with self.assertRaises(ValueError):
            get_total_number_of_sequences(2, -1)

    def test_invalid_input_m_negative_n_negative(self):
        with self.assertRaises(ValueError):
            get_total_number_of_sequences(-1, -1)
