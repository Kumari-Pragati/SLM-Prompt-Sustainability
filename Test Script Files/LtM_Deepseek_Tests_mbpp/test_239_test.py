import unittest
from mbpp_239_code import get_total_number_of_sequences

class TestGetTotalNumberOfSequences(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(get_total_number_of_sequences(1, 1), 1)
        self.assertEqual(get_total_number_of_sequences(2, 2), 2)

    def test_edge_conditions(self):
        self.assertEqual(get_total_number_of_sequences(0, 1), 0)
        self.assertEqual(get_total_number_of_sequences(1, 0), 0)
        self.assertEqual(get_total_number_of_sequences(0, 0), 0)
        self.assertEqual(get_total_number_of_sequences(1, 1), 1)

    def test_boundary_conditions(self):
        self.assertEqual(get_total_number_of_sequences(2, 1), 2)
        self.assertEqual(get_total_number_of_sequences(1, 2), 1)
        self.assertEqual(get_total_number_of_sequences(2, 2), 2)

    def test_complex_cases(self):
        self.assertEqual(get_total_number_of_sequences(3, 2), 4)
        self.assertEqual(get_total_number_of_sequences(2, 3), 2)
        self.assertEqual(get_total_number_of_sequences(3, 3), 6)
