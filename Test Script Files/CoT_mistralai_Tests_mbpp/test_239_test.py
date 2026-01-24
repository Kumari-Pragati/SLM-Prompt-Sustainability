import unittest
from mbpp_239_code import get_total_number_of_sequences

class TestGetTotalNumberOfSequences(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(get_total_number_of_sequences(3, 2), 3)
        self.assertEqual(get_total_number_of_sequences(4, 3), 10)
        self.assertEqual(get_total_number_of_sequences(5, 4), 27)

    def test_edge_case(self):
        self.assertEqual(get_total_number_of_sequences(0, 0), 0)
        self.assertEqual(get_total_number_of_sequences(1, 0), 0)
        self.assertEqual(get_total_number_of_sequences(0, 1), 0)

    def test_boundary_case(self):
        self.assertEqual(get_total_number_of_sequences(1, 1), 1)
        self.assertEqual(get_total_number_of_sequences(2, 1), 2)
        self.assertEqual(get_total_number_of_sequences(1, 2), 1)

    def test_invalid_input(self):
        self.assertRaises(ValueError, get_total_number_of_sequences, -1, 2)
        self.assertRaises(ValueError, get_total_number_of_sequences, 2, -1)
        self.assertRaises(ValueError, get_total_number_of_sequences, 0, 0)
