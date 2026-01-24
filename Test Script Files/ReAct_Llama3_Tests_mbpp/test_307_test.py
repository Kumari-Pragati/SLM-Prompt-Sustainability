import unittest
from mbpp_307_code import colon_tuplex

class TestColonTuplex(unittest.TestCase):
    def test_typical_case(self):
        tuplex = [(1, 2), (3, 4)]
        m = 0
        n = 5
        result = colon_tuplex(tuplex, m, n)
        self.assertEqual(result, [(1, 2), (3, 4), (1, 2, 5)])

    def test_edge_case_m_out_of_range(self):
        tuplex = [(1, 2), (3, 4)]
        m = 1
        n = 5
        result = colon_tuplex(tuplex, m, n)
        self.assertEqual(result, [(1, 2), (3, 4), (3, 4, 5)])

    def test_edge_case_m_zero(self):
        tuplex = [(1, 2), (3, 4)]
        m = 0
        n = 5
        result = colon_tuplex(tuplex, m, n)
        self.assertEqual(result, [(1, 2), (3, 4), (1, 2, 5)]

    def test_edge_case_m_negative(self):
        tuplex = [(1, 2), (3, 4)]
        m = -1
        n = 5
        with self.assertRaises(IndexError):
            colon_tuplex(tuplex, m, n)

    def test_edge_case_n_out_of_range(self):
        tuplex = [(1, 2), (3, 4)]
        m = 0
        n = 10
        result = colon_tuplex(tuplex, m, n)
        self.assertEqual(result, [(1, 2), (3, 4), (1, 2, 5)]

    def test_edge_case_n_zero(self):
        tuplex = [(1, 2), (3, 4)]
        m = 0
        n = 0
        result = colon_tuplex(tuplex, m, n)
        self.assertEqual(result, [(1, 2), (3, 4)]

    def test_edge_case_n_negative(self):
        tuplex = [(1, 2), (3, 4)]
        m = 0
        n = -5
        with self.assertRaises(TypeError):
            colon_tuplex(tuplex, m, n)
