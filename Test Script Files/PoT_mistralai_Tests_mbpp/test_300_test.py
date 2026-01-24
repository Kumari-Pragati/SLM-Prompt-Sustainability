import unittest
from mbpp_300_code import count_binary_seq

class TestCountBinarySeq(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(count_binary_seq(1), 1)
        self.assertEqual(count_binary_seq(2), 3)
        self.assertEqual(count_binary_seq(3), 7)
        self.assertEqual(count_binary_seq(4), 15)
        self.assertEqual(count_binary_seq(5), 31)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(count_binary_seq(0), 0)
        self.assertEqual(count_binary_seq(6), 63)
        self.assertEqual(count_binary_seq(7), 127)
        self.assertEqual(count_binary_seq(8), 255)
        self.assertEqual(count_binary_seq(9), 511)
