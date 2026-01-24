import unittest
from mbpp_239_code import get_total_number_of_sequences

class TestGetTotalNumberOfSequences(unittest.TestCase):

    def test_get_total_number_of_sequences_with_zero(self):
        self.assertEqual(get_total_number_of_sequences(0, 0), 0)

    def test_get_total_number_of_sequences_with_one_dimension(self):
        self.assertEqual(get_total_number_of_sequences(1, 1), 1)
        self.assertEqual(get_total_number_of_sequences(1, 2), 2)
        self.assertEqual(get_total_number_of_sequences(1, 3), 4)

    def test_get_total_number_of_sequences_with_two_dimensions(self):
        self.assertEqual(get_total_number_of_sequences(2, 1), 2)
        self.assertEqual(get_total_number_of_sequences(2, 2), 5)
        self.assertEqual(get_total_number_of_sequences(2, 3), 14)
        self.assertEqual(get_total_number_of_sequences(3, 3), 28)
