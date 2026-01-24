import unittest
from mbpp_300_code import count_binary_seq

class TestCountBinarySeq(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_binary_seq(2), 5)
        self.assertEqual(count_binary_seq(3), 14)
        self.assertEqual(count_binary_seq(4), 30)

    def test_edge_cases(self):
        self.assertEqual(count_binary_seq(0), 1)
        self.assertEqual(count_binary_seq(1), 1)
        self.assertEqual(count_binary_seq(5), 56)

    def test_large_input(self):
        self.assertAlmostEqual(count_binary_seq(100), 1.3378387890625e+62, delta=1)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            count_binary_seq(-1)
