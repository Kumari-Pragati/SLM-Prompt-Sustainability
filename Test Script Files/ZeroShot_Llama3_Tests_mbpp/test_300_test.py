import unittest
from mbpp_300_code import count_binary_seq

class TestCountBinarySeq(unittest.TestCase):

    def test_count_binary_seq(self):
        self.assertEqual(count_binary_seq(0), 1)
        self.assertEqual(count_binary_seq(1), 2)
        self.assertEqual(count_binary_seq(2), 4)
        self.assertEqual(count_binary_seq(3), 9)
        self.assertEqual(count_binary_seq(4), 16)
        self.assertEqual(count_binary_seq(5), 31)
        self.assertEqual(count_binary_seq(6), 64)
        self.assertEqual(count_binary_seq(7), 127)
        self.assertEqual(count_binary_seq(8), 256)
        self.assertEqual(count_binary_seq(9), 511)
        self.assertEqual(count_binary_seq(10), 1024)

    def test_count_binary_seq_edge_cases(self):
        self.assertEqual(count_binary_seq(-1), 1)
        self.assertEqual(count_binary_seq(-2), 1)
        self.assertEqual(count_binary_seq(-3), 1)
        self.assertEqual(count_binary_seq(-4), 1)
        self.assertEqual(count_binary_seq(-5), 1)
        self.assertEqual(count_binary_seq(-6), 1)
        self.assertEqual(count_binary_seq(-7), 1)
        self.assertEqual(count_binary_seq(-8), 1)
        self.assertEqual(count_binary_seq(-9), 1)
        self.assertEqual(count_binary_seq(-10), 1)
