import unittest
from mbpp_300_code import count_binary_seq

class TestCountBinarySeq(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count_binary_seq(0), 1)
        self.assertEqual(count_binary_seq(1), 2)

    def test_edge_conditions(self):
        self.assertEqual(count_binary_seq(2), 6)

    def test_complex_cases(self):
        self.assertEqual(count_binary_seq(3), 20)
