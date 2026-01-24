import unittest
from mbpp_300_code import count_binary_seq

class TestCountBinarySeq(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(count_binary_seq(3), 5)
        self.assertEqual(count_binary_seq(4), 14)
        self.assertEqual(count_binary_seq(5), 35)

    def test_zero(self):
        self.assertEqual(count_binary_seq(0), 1)

    def test_negative_integer(self):
        self.assertRaises(ValueError, count_binary_seq, -1)

    def test_fractional_input(self):
        self.assertRaises(TypeError, count_binary_seq, 2.5)
