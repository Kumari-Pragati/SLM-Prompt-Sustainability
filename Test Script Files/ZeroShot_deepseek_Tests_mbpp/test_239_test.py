import unittest
from mbpp_239_code import get_total_number_of_sequences

class TestGetTotalNumberOfSequences(unittest.TestCase):

    def test_get_total_number_of_sequences(self):
        self.assertEqual(get_total_number_of_sequences(0, 0), 0)
        self.assertEqual(get_total_number_of_sequences(1, 1), 1)
        self.assertEqual(get_total_number_of_sequences(2, 2), 2)
        self.assertEqual(get_total_number_of_sequences(3, 3), 4)
        self.assertEqual(get_total_number_of_sequences(4, 4), 8)
        self.assertEqual(get_total_number_of_sequences(5, 5), 16)
        self.assertEqual(get_total_number_of_sequences(6, 6), 32)
        self.assertEqual(get_total_number_of_sequences(7, 7), 64)
        self.assertEqual(get_total_number_of_sequences(8, 8), 128)
        self.assertEqual(get_total_number_of_sequences(9, 9), 256)
        self.assertEqual(get_total_number_of_sequences(10, 10), 512)
