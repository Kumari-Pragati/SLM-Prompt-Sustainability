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

    def test_edge_cases(self):
        self.assertEqual(sequence(0), 1)  # Edge case: n == 0
        self.assertEqual(sequence(-1), 1)  # Edge case: n < 0

    def test_corner_cases(self):
        self.assertEqual(sequence(8), 11)  # Corner case: n == 8
        self.assertEqual(sequence(10), 11)  # Corner case: n == 10
