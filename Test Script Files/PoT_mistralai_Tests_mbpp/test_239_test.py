import unittest
from mbpp_239_code import get_total_number_of_sequences

class TestGetTotalNumberOfSequences(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(get_total_number_of_sequences(1, 1), 1)
        self.assertEqual(get_total_number_of_sequences(2, 2), 3)
        self.assertEqual(get_total_number_of_sequences(3, 3), 8)
        self.assertEqual(get_total_number_of_sequences(4, 4), 27)
        self.assertEqual(get_total_number_of_sequences(5, 5), 89)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(get_total_number_of_sequences(0, 0), 0)
        self.assertEqual(get_total_number_of_sequences(0, 1), 0)
        self.assertEqual(get_total_number_of_sequences(1, 0), 0)
        self.assertEqual(get_total_number_of_sequences(1, 2), 2)
        self.assertEqual(get_total_number_of_sequences(2, 0), 0)
        self.assertEqual(get_total_number_of_sequences(2, 3), 7)
        self.assertEqual(get_total_number_of_sequences(3, 0), 0)
        self.assertEqual(get_total_number_of_sequences(3, 4), 26)
        self.assertEqual(get_total_number_of_sequences(4, 0), 0)
        self.assertEqual(get_total_number_of_sequences(4, 5), 102)
