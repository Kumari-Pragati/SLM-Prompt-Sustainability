import unittest
from mbpp_239_code import get_total_number_of_sequences

class TestGetTotalNumberOfSequences(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_total_number_of_sequences(3, 4), 7)

    def test_edge_case_m_zero(self):
        self.assertEqual(get_total_number_of_sequences(0, 4), 0)

    def test_edge_case_n_zero(self):
        self.assertEqual(get_total_number_of_sequences(3, 0), 0)

    def test_edge_case_m_and_n_zero(self):
        self.assertEqual(get_total_number_of_sequences(0, 0), 0)

    def test_edge_case_m_one(self):
        self.assertEqual(get_total_number_of_sequences(1, 4), 1)

    def test_edge_case_n_one(self):
        self.assertEqual(get_total_number_of_sequences(3, 1), 3)

    def test_edge_case_m_and_n_one(self):
        self.assertEqual(get_total_number_of_sequences(1, 1), 1)

    def test_edge_case_m_and_n_two(self):
        self.assertEqual(get_total_number_of_sequences(2, 2), 3)

    def test_edge_case_m_and_n_three(self):
        self.assertEqual(get_total_number_of_sequences(3, 3), 6)

    def test_edge_case_m_and_n_four(self):
        self.assertEqual(get_total_number_of_sequences(4, 4), 10)

    def test_edge_case_m_and_n_five(self):
        self.assertEqual(get_total_number_of_sequences(5, 5), 15)

    def test_edge_case_m_and_n_six(self):
        self.assertEqual(get_total_number_of_sequences(6, 6), 21)

    def test_edge_case_m_and_n_seven(self):
        self.assertEqual(get_total_number_of_sequences(7, 7), 28)

    def test_edge_case_m_and_n_eight(self):
        self.assertEqual(get_total_number_of_sequences(8, 8), 36)

    def test_edge_case_m_and_n_nine(self):
        self.assertEqual(get_total_number_of_sequences(9, 9), 45)

    def test_edge_case_m_and_n_ten(self):
        self.assertEqual(get_total_number_of_sequences(10, 10), 55)
