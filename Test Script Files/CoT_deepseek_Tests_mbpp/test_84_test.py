import unittest
from mbpp_84_code import sequence

class TestSequence(unittest.TestCase):

    def test_sequence_typical_cases(self):
        self.assertEqual(sequence(1), 1)
        self.assertEqual(sequence(2), 1)
        self.assertEqual(sequence(3), 2)
        self.assertEqual(sequence(4), 4)
        self.assertEqual(sequence(5), 5)
        self.assertEqual(sequence(6), 7)
        self.assertEqual(sequence(7), 10)

    def test_sequence_edge_cases(self):
        self.assertEqual(sequence(0), 1)
        self.assertEqual(sequence(-1), 1)
        self.assertEqual(sequence(-10), 1)

    def test_sequence_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sequence('a')
        with self.assertRaises(TypeError):
            sequence(None)
        with self.assertRaises(TypeError):
            sequence([])
        with self.assertRaises(TypeError):
            sequence({})
