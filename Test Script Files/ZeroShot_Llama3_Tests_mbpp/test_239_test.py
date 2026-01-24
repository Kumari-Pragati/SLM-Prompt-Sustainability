import unittest
from mbpp_239_code import get_total_number_of_sequences

class TestGetTotalNumberOfSequences(unittest.TestCase):

    def test_get_total_number_of_sequences_1(self):
        self.assertEqual(get_total_number_of_sequences(1, 1), 1)

    def test_get_total_number_of_sequences_2(self):
        self.assertEqual(get_total_number_of_sequences(2, 1), 1)

    def test_get_total_number_of_sequences_3(self):
        self.assertEqual(get_total_number_of_sequences(1, 2), 1)

    def test_get_total_number_of_sequences_4(self):
        self.assertEqual(get_total_number_of_sequences(2, 2), 2)

    def test_get_total_number_of_sequences_5(self):
        self.assertEqual(get_total_number_of_sequences(3, 2), 3)

    def test_get_total_number_of_sequences_6(self):
        self.assertEqual(get_total_number_of_sequences(2, 3), 3)

    def test_get_total_number_of_sequences_7(self):
        self.assertEqual(get_total_number_of_sequences(3, 3), 4)

    def test_get_total_number_of_sequences_8(self):
        self.assertEqual(get_total_number_of_sequences(4, 3), 7)

    def test_get_total_number_of_sequences_9(self):
        self.assertEqual(get_total_number_of_sequences(3, 4), 7)

    def test_get_total_number_of_sequences_10(self):
        self.assertEqual(get_total_number_of_sequences(4, 4), 8)
