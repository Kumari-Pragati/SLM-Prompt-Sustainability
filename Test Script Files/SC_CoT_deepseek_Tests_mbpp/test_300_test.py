import unittest
from mbpp_300_code import count_binary_seq

class TestCountBinarySeq(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_binary_seq(3), 15)

    def test_edge_case(self):
        self.assertEqual(count_binary_seq(0), 1)

    def test_boundary_case(self):
        self.assertEqual(count_binary_seq(1), 2)

    def test_special_case(self):
        self.assertEqual(count_binary_seq(2), 6)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_binary_seq('a')

        with self.assertRaises(ValueError):
            count_binary_seq(-1)
