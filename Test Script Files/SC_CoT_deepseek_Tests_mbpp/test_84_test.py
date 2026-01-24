import unittest
from mbpp_84_code import sequence

class TestSequence(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(sequence(1), 1)
        self.assertEqual(sequence(2), 1)
        self.assertEqual(sequence(3), 2)
        self.assertEqual(sequence(4), 4)
        self.assertEqual(sequence(5), 5)
        self.assertEqual(sequence(6), 7)
        self.assertEqual(sequence(7), 10)
        self.assertEqual(sequence(8), 14)

    def test_boundary_conditions(self):
        self.assertEqual(sequence(0), 1)
        self.assertEqual(sequence(-1), 1)

    def test_edge_cases(self):
        self.assertEqual(sequence(30), 102334155)
        self.assertEqual(sequence(40), 1677631803519440038883677889)

    def test_invalid_inputs(self):
        with self.assertRaises(RecursionError):
            sequence(1000)  # This should exceed Python's recursion limit
