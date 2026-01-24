import unittest
from mbpp_307_code import colon_tuplex

class TestColonTuplex(unittest.TestCase):

    def test_typical_case(self):
        tuplex = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
        m = 1
        n = 10
        expected_output = ([1, 2, 3], [4, 5, 6, 10], [7, 8, 9])
        self.assertEqual(colon_tuplex(tuplex, m, n), expected_output)

    def test_edge_case_m_equals_0(self):
        tuplex = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
        m = 0
        n = 10
        expected_output = ([1, 2, 3], [4, 5, 6, 10], [7, 8, 9])
        self.assertEqual(colon_tuplex(tuplex, m, n), expected_output)

    def test_edge_case_m_equals_last_index(self):
        tuplex = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
        m = 2
        n = 10
        expected_output = ([1, 2, 3], [4, 5, 6], [7, 8, 9, 10])
        self.assertEqual(colon_tuplex(tuplex, m, n), expected_output)

    def test_invalid_m_greater_than_length(self):
        tuplex = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
        m = 3
        n = 10
        with self.assertRaises(IndexError):
            colon_tuplex(tuplex, m, n)

    def test_invalid_m_less_than_0(self):
        tuplex = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
        m = -1
        n = 10
        with self.assertRaises(IndexError):
            colon_tuplex(tuplex, m, n)
