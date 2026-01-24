import unittest
from mbpp_300_code import count_binary_seq

class TestCountBinarySeq(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_binary_seq(0), 1)
        self.assertEqual(count_binary_seq(1), 1)
        self.assertEqual(count_binary_seq(2), 5)
        self.assertEqual(count_binary_seq(3), 14)
        self.assertEqual(count_binary_seq(4), 34)

    def test_edge_cases(self):
        self.assertEqual(count_binary_seq(-1), 1)
        self.assertEqual(count_binary_seq(0.5), 1)
        self.assertEqual(count_binary_seq(0.5), 1)

    def test_corner_cases(self):
        self.assertEqual(count_binary_seq(5), 89)
        self.assertEqual(count_binary_seq(10), 742)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_binary_seq('a')
        with self.assertRaises(TypeError):
            count_binary_seq(None)
