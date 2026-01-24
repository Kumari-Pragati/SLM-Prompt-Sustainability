import unittest
from mbpp_84_code import sequence

class TestSequence(unittest.TestCase):

    def test_sequence_typical(self):
        self.assertEqual(sequence(1), 1)
        self.assertEqual(sequence(2), 1)
        self.assertEqual(sequence(3), 2)
        self.assertEqual(sequence(4), 3)

    def test_sequence_edge(self):
        self.assertEqual(sequence(0), 1)
        self.assertEqual(sequence(5), 5)

    def test_sequence_negative(self):
        with self.assertRaisesRecursionError:
            sequence(-1)

    def test_sequence_non_integer(self):
        with self.assertRaisesRecursionError:
            sequence(3.5)

    def test_sequence_large(self):
        self.assertEqual(sequence(100), 354224848179261915075)

    def test_sequence_recursive(self):
        self.assertEqual(sequence(10), 34)
