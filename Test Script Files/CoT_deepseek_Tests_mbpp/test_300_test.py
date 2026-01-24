import unittest
from mbpp_300_code import count_binary_seq

class TestCountBinarySeq(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_binary_seq(3), 14)

    def test_zero_input(self):
        self.assertEqual(count_binary_seq(0), 1)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            count_binary_seq(-1)

    def test_large_input(self):
        self.assertGreater(count_binary_seq(20), 0)

    def test_float_input(self):
        with self.assertRaises(TypeError):
            count_binary_seq(2.5)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            count_binary_seq('2')
