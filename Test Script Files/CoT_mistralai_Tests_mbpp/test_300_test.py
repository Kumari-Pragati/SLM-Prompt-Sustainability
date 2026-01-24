import unittest
from mbpp_300_code import count_binary_seq

class TestCountBinarySeq(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(count_binary_seq(3), 18)
        self.assertEqual(count_binary_seq(5), 105)

    def test_edge_cases(self):
        self.assertEqual(count_binary_seq(0), 1)
        self.assertEqual(count_binary_seq(1), 1)
        self.assertEqual(count_binary_seq(2), 5)

    def test_boundary_conditions(self):
        self.assertEqual(count_binary_seq(-1), None)
        self.assertEqual(count_binary_seq(float('inf')), None)
        self.assertEqual(count_binary_seq(complex(0, 0)), None)
        self.assertEqual(count_binary_seq('str'), None)
        self.assertEqual(count_binary_seq(None), None)
