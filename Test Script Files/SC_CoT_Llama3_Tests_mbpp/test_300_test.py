import unittest
from mbpp_300_code import count_binary_seq

class TestCountBinarySeq(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(count_binary_seq(5), 61)

    def test_edge_case_n_zero(self):
        self.assertEqual(count_binary_seq(0), 1)

    def test_edge_case_n_one(self):
        self.assertEqual(count_binarySeq(1), 1)

    def test_edge_case_n_two(self):
        self.assertEqual(count_binarySeq(2), 5)

    def test_edge_case_n_negative(self):
        with self.assertRaises(ValueError):
            count_binary_seq(-1)

    def test_edge_case_n_non_integer(self):
        with self.assertRaises(TypeError):
            count_binary_seq('a')

    def test_edge_case_r_zero(self):
        with self.assertRaises(ZeroDivisionError):
            count_binary_seq(5, r=0)

    def test_edge_case_r_negative(self):
        with self.assertRaises(ValueError):
            count_binarySeq(5, r=-1)

    def test_edge_case_r_non_integer(self):
        with self.assertRaises(TypeError):
            count_binarySeq(5, r='a')
