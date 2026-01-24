import unittest
from mbpp_300_code import count_binary_seq

class TestCountBinarySeq(unittest.TestCase):

    def test_zero_input(self):
        self.assertEqual(count_binary_seq(0), 1)

    def test_one_input(self):
        self.assertEqual(count_binarySeq(1), 1)

    def test_small_input(self):
        self.assertEqual(count_binarySeq(5), 30)

    def test_large_input(self):
        self.assertEqual(count_binarySeq(10), 742)

    def test_negative_input(self):
        with self.assertRaises(TypeError):
            count_binarySeq(-1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            count_binarySeq('a')
