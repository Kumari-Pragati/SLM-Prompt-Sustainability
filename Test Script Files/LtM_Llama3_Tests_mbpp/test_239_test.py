import unittest
from mbpp_239_code import get_total_number_of_sequences

class TestGetTotalNumberOfSequences(unittest.TestCase):
    def test_zero_input(self):
        self.assertEqual(get_total_number_of_sequences(0, 0), 0)

    def test_single_input(self):
        self.assertEqual(get_total_number_of_sequences(1, 1), 1)

    def test_zero_m(self):
        self.assertEqual(get_total_number_of_sequences(0, 1), 0)

    def test_zero_n(self):
        self.assertEqual(get_total_number_of_sequences(1, 0), 0)

    def test_edge_case_m(self):
        self.assertEqual(get_total_number_of_sequences(1, 2), 1)

    def test_edge_case_n(self):
        self.assertEqual(get_total_number_of_sequences(2, 1), 1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            get_total_number_of_sequences('a', 1)

    def test_negative_input(self):
        with self.assertRaises(TypeError):
            get_total_number_of_sequences(-1, 1)

    def test_non_integer_m_and_n(self):
        with self.assertRaises(TypeError):
            get_total_number_of_sequences('a', 'b')

    def test_large_input(self):
        self.assertEqual(get_total_number_of_sequences(10, 10), 55)
