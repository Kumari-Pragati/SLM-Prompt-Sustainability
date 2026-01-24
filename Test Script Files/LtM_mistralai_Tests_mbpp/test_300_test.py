import unittest
from mbpp_300_code import count_binary_seq

class TestCountBinarySeq(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(count_binary_seq(1), 1)
        self.assertEqual(count_binary_seq(2), 2)
        self.assertEqual(count_binary_seq(3), 4)

    def test_edge_cases(self):
        self.assertEqual(count_binary_seq(0), 0)
        self.assertEqual(count_binary_seq(4), 7)
        self.assertEqual(count_binary_seq(5), 15)

    def test_complex(self):
        self.assertEqual(count_binary_seq(10), 1023)
        self.assertEqual(count_binary_seq(20), 65533)
        self.assertEqual(count_binary_seq(30), 2097151)
