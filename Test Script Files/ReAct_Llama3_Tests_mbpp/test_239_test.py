import unittest
from mbpp_239_code import get_total_number_of_sequences

class TestGetTotalNumberOfSequences(unittest.TestCase):
    def test_zero_input(self):
        self.assertEqual(get_total_number_of_sequences(0, 0), 0)

    def test_single_input(self):
        self.assertEqual(get_total_number_of_sequences(1, 1), 1)

    def test_small_input(self):
        self.assertEqual(get_total_number_of_sequences(2, 2), 2)

    def test_large_input(self):
        self.assertEqual(get_total_number_of_sequences(5, 5), 16)

    def test_edge_case_m_zero(self):
        self.assertEqual(get_total_number_of_sequences(0, 3), 0)

    def test_edge_case_n_zero(self):
        self.assertEqual(get_total_number_of_sequences(4, 0), 0)

    def test_edge_case_m_one(self):
        self.assertEqual(get_total_number_of_sequences(1, 3), 1)

    def test_edge_case_n_one(self):
        self.assertEqual(get_total_number_of_sequences(4, 1), 1)

    def test_edge_case_m_and_n_zero(self):
        self.assertEqual(get_total_number_of_sequences(0, 0), 0)

    def test_edge_case_m_and_n_one(self):
        self.assertEqual(get_total_number_of_sequences(1, 1), 1)
