import unittest
from mbpp_923_code import super_seq

class TestSuperSeq(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(super_seq('abc', 'def', 3, 3), 4)

    def test_edge_case_m_zero(self):
        self.assertEqual(super_seq('abc', 'def', 0, 3), 3)

    def test_edge_case_n_zero(self):
        self.assertEqual(super_seq('abc', 'def', 3, 0), 3)

    def test_edge_case_m_and_n_zero(self):
        self.assertEqual(super_seq('abc', 'def', 0, 0), 0)

    def test_edge_case_m_one(self):
        self.assertEqual(super_seq('abc', 'def', 1, 3), 1)

    def test_edge_case_n_one(self):
        self.assertEqual(super_seq('abc', 'def', 3, 1), 1)

    def test_edge_case_m_and_n_one(self):
        self.assertEqual(super_seq('abc', 'def', 1, 1), 1)

    def test_super_seq_with_matching_chars(self):
        self.assertEqual(super_seq('abc', 'def', 3, 3), 4)

    def test_super_seq_with_non_matching_chars(self):
        self.assertEqual(super_seq('abc', 'def', 3, 3), 4)

    def test_super_seq_with_empty_strings(self):
        self.assertEqual(super_seq('', 'def', 0, 3), 3)

    def test_super_seq_with_invalid_inputs(self):
        with self.assertRaises(TypeError):
            super_seq(123, 'def', 3, 3)
