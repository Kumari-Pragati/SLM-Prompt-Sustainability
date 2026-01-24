import unittest
from mbpp_300_code import count_binary_seq

class TestCountBinarySeq(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_binary_seq(1), 2)
        self.assertEqual(count_binary_seq(2), 6)
        self.assertEqual(count_binary_seq(3), 20)

    def test_edge_cases(self):
        self.assertEqual(count_binary_seq(0), 1)
        self.assertEqual(count_binary_seq(10), 165)

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            count_binary_seq('a')
        with self.assertRaises(ValueError):
            count_binary_seq(-1)
