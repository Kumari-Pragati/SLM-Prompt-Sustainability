import unittest
from mbpp_300_code import count_binary_seq

class TestCountBinarySeq(unittest.TestCase):

    def test_count_binary_seq_small_numbers(self):
        self.assertEqual(count_binary_seq(0), 1)
        self.assertEqual(count_binary_seq(1), 2)
        self.assertEqual(count_binary_seq(2), 5)

    def test_count_binary_seq_large_numbers(self):
        self.assertEqual(count_binary_seq(10), 16400)
        self.assertEqual(count_binary_seq(20), 1070379000)
