import unittest
from mbpp_239_code import get_total_number_of_sequences

class TestGetTotalNumberOfSequences(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(get_total_number_of_sequences(3, 4), 7)

    def test_edge_case_m_zero(self):
        self.assertEqual(get_total_number_of_sequences(0, 4), 0)

    def test_edge_case_n_zero(self):
        self.assertEqual(get_total_number_of_sequences(3, 0), 0)

    def test_edge_case_m_n_zero(self):
        self.assertEqual(get_total_number_of_sequences(0, 0), 0)

    def test_edge_case_m_one(self):
        self.assertEqual(get_total_number_of_sequences(1, 4), 1)

    def test_edge_case_n_one(self):
        self.assertEqual(get_total_number_of_sequences(3, 1), 3)

    def test_edge_case_m_n_one(self):
        self.assertEqual(get_total_number_of_sequences(1, 1), 1)

    def test_edge_case_m_half_n(self):
        self.assertEqual(get_total_number_of_sequences(3, 2), 3)

    def test_edge_case_m_n_half(self):
        self.assertEqual(get_total_number_of_sequences(2, 4), 2)

    def test_edge_case_m_n_half(self):
        self.assertEqual(get_total_number_of_sequences(3, 3), 3)

    def test_invalid_input_m_negative(self):
        with self.assertRaises(ValueError):
            get_total_number_of_sequences(-1, 4)

    def test_invalid_input_n_negative(self):
        with self.assertRaises(ValueError):
            get_total_number_of_sequences(3, -1)

    def test_invalid_input_m_n_negative(self):
        with self.assertRaises(ValueError):
            get_total_number_of_sequences(-1, -1)
