import unittest
from mbpp_300_code import count_binary_seq

class TestCountBinarySeq(unittest.TestCase):
    def test_small_positive_input(self):
        self.assertEqual(count_binary_seq(3), 14)

    def test_large_positive_input(self):
        self.assertEqual(count_binary_seq(10), 742)

    def test_zero_input(self):
        self.assertEqual(count_binary_seq(0), 1)

    def test_negative_input(self):
        with self.assertRaises(TypeError):
            count_binary_seq(-1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            count_binary_seq(3.5)
