import unittest
from mbpp_300_code import count_binary_seq

class TestCountBinarySeq(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(count_binary_seq(0), 1)
        self.assertEqual(count_binary_seq(1), 1)
        self.assertEqual(count_binary_seq(2), 5)

    def test_edge_cases(self):
        self.assertEqual(count_binary_seq(-1), 1)
        self.assertEqual(count_binary_seq(0.5), 1)
        self.assertEqual(count_binary_seq(0.5), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_binary_seq('a')
        with self.assertRaises(TypeError):
            count_binary_seq(None)
