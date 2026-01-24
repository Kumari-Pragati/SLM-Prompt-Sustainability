import unittest
from mbpp_84_code import sequence

class TestSequence(unittest.TestCase):

    def test_sequence_base_cases(self):
        self.assertEqual(sequence(1), 1)
        self.assertEqual(sequence(2), 1)

    def test_sequence_recursive(self):
        self.assertEqual(sequence(3), 2)
        self.assertEqual(sequence(4), 3)
        self.assertEqual(sequence(5), 5)

    def test_sequence_edge_cases(self):
        self.assertEqual(sequence(0), 1)
        self.assertEqual(sequence(-1), 1)

    def test_sequence_invalid_input(self):
        with self.assertRaises RecursionError:
            sequence(1000)
