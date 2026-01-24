import unittest
from mbpp_84_code import sequence

class TestSequence(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(sequence(1), 1)
        self.assertEqual(sequence(2), 1)

    def test_edge_and_boundary(self):
        self.assertEqual(sequence(0), None)
        self.assertEqual(sequence(-1), None)
        self.assertEqual(sequence(3), 1)
        self.assertEqual(sequence(4), 2)
        self.assertEqual(sequence(5), 3)

    def test_complex(self):
        self.assertEqual(sequence(6), 5)
        self.assertEqual(sequence(7), 8)
        self.assertEqual(sequence(8), 13)
        self.assertEqual(sequence(9), 21)
        self.assertEqual(sequence(10), 34)
