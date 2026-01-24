import unittest
from mbpp_239_code import get_total_number_of_sequences

class TestGetTotalNumberOfSequences(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(get_total_number_of_sequences(3, 4), 7)

    def test_edge_case_m_zero(self):
        self.assertEqual(get_total_number_of_sequences(0, 4), 0)

    def test_edge_case_n_zero(self):
        self.assertEqual(get_total_number_of_sequences(3, 0), 0)

    def test_edge_case_m_one(self):
        self.assertEqual(get_total_number_of_sequences(1, 4), 1)

    def test_edge_case_n_one(self):
        self.assertEqual(get_total_number_of_sequences(3, 1), 3)

    def test_edge_case_m_and_n_one(self):
        self.assertEqual(get_total_number_of_sequences(1, 1), 1)

    def test_edge_case_m_and_n_zero(self):
        self.assertEqual(get_total_number_of_sequences(0, 0), 0)
