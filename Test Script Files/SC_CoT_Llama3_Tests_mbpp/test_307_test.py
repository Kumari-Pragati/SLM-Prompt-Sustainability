import unittest
from mbpp_307_code import colon_tuplex

class TestColonTuplex(unittest.TestCase):

    def test_typical_input(self):
        tuplex = ({1, 2, 3}, {4, 5, 6})
        m = 0
        n = 7
        result = colon_tuplex(tuplex, m, n)
        self.assertEqual(result, ({1, 2, 3}, {4, 5, 6, 7}))

    def test_edge_case_m_out_of_range(self):
        tuplex = ({1, 2, 3}, {4, 5, 6})
        m = 1
        n = 7
        result = colon_tuplex(tuplex, m, n)
        self.assertEqual(result, ({1, 2, 3}, {4, 5, 6, 7}))

    def test_edge_case_m_zero(self):
        tuplex = ({1, 2, 3}, {4, 5, 6})
        m = 0
        n = 7
        result = colon_tuplex(tuplex, m, n)
        self.assertEqual(result, ({1, 2, 3}, {4, 5, 6, 7}))

    def test_edge_case_m_negative(self):
        tuplex = ({1, 2, 3}, {4, 5, 6})
        m = -1
        n = 7
        with self.assertRaises(IndexError):
            colon_tuplex(tuplex, m, n)

    def test_edge_case_n_non_integer(self):
        tuplex = ({1, 2, 3}, {4, 5, 6})
        m = 0
        n ='seven'
        with self.assertRaises(TypeError):
            colon_tuplex(tuplex, m, n)

    def test_edge_case_n_zero(self):
        tuplex = ({1, 2, 3}, {4, 5, 6})
        m = 0
        n = 0
        result = colon_tuplex(tuplex, m, n)
        self.assertEqual(result, ({1, 2, 3}, {4, 5, 6}))

    def test_edge_case_n_negative(self):
        tuplex = ({1, 2, 3}, {4, 5, 6})
        m = 0
        n = -7
        result = colon_tuplex(tuplex, m, n)
        self.assertEqual(result, ({1, 2, 3}, {4, 5, 6, -7}))
