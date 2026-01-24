import unittest
from mbpp_84_code import sequence

class TestSequence(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(sequence(1), 1)
        self.assertEqual(sequence(2), 1)
        self.assertEqual(sequence(3), 2)
        self.assertEqual(sequence(4), 3)
        self.assertEqual(sequence(5), 5)
        self.assertEqual(sequence(6), 8)
        self.assertEqual(sequence(7), 13)
        self.assertEqual(sequence(8), 21)
        self.assertEqual(sequence(9), 34)
        self.assertEqual(sequence(10), 55)

    def test_edge_and_boundary(self):
        self.assertEqual(sequence(0), 0)
        self.assertEqual(sequence(-1), 0)
        self.assertEqual(sequence(21), 133)
        self.assertEqual(sequence(22), 233)
        self.assertEqual(sequence(33), 2075)
        self.assertEqual(sequence(34), 3776)
