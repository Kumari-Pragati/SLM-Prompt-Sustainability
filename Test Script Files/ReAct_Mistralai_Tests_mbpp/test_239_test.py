import unittest
from mbpp_239_code import get_total_number_of_sequences

class TestGetTotalNumberOfSequences(unittest.TestCase):

    def test_empty_sequences(self):
        self.assertEqual(get_total_number_of_sequences(0, 0), 0)

    def test_single_sequence(self):
        for m in range(1, 6):
            self.assertEqual(get_total_number_of_sequences(m, 0), m)
            self.assertEqual(get_total_number_of_sequences(0, m), 0)

    def test_small_sequences(self):
        for m in range(1, 6):
            for n in range(1, m+1):
                self.assertEqual(get_total_number_of_sequences(m, n),
                                 get_total_number_of_sequences(m-1, n) +
                                 get_total_number_of_sequences(m, n-1))

    def test_large_sequences(self):
        for m in range(10, 100, 10):
            for n in range(1, m+1):
                self.assertEqual(get_total_number_of_sequences(m, n),
                                 get_total_number_of_sequences(m-1, n) +
                                 get_total_number_of_sequences(m, n-1))

    def test_negative_arguments(self):
        self.assertRaises(ValueError, get_total_number_of_sequences, -1, 1)
        self.assertRaises(ValueError, get_total_number_of_sequences, 1, -1)
