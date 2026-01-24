import unittest
from mbpp_300_code import count_binary_seq

class TestCountBinarySeq(unittest.TestCase):

    def test_count_binary_seq_with_zero(self):
        self.assertEqual(count_binary_seq(0), 1)

    def test_count_binary_seq_with_one(self):
        self.assertEqual(count_binary_seq(1), 1)

    def test_count_binary_seq_with_two(self):
        self.assertEqual(count_binary_seq(2), 3)

    def test_count_binary_seq_with_three(self):
        self.assertEqual(count_binary_seq(3), 7)

    def test_count_binary_seq_with_four(self):
        self.assertEqual(count_binary_seq(4), 15)

    def test_count_binary_seq_with_five(self):
        self.assertEqual(count_binary_seq(5), 31)

    def test_count_binary_seq_with_large_number(self):
        self.assertEqual(count_binary_seq(100), 12676506002282212175)
