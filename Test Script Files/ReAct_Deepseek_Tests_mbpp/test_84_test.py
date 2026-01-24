import unittest
from mbpp_84_code import sequence

class TestSequenceFunction(unittest.TestCase):

    def test_sequence_typical_cases(self):
        self.assertEqual(sequence(1), 1)
        self.assertEqual(sequence(2), 1)
        self.assertEqual(sequence(3), 2)
        self.assertEqual(sequence(4), 4)
        self.assertEqual(sequence(5), 5)
        self.assertEqual(sequence(6), 7)
        self.assertEqual(sequence(7), 10)

    def test_sequence_edge_cases(self):
        self.assertEqual(sequence(0), 1)  # Edge case: n == 0
        self.assertEqual(sequence(-1), 1)  # Edge case: n < 1
        self.assertEqual(sequence(8), 11)  # Edge case: n > 2

    def test_sequence_error_cases(self):
        with self.assertRaises(TypeError):
            sequence('a')  # Error case: non-integer input
        with self.assertRaises(TypeError):
            sequence(None)  # Error case: None input
