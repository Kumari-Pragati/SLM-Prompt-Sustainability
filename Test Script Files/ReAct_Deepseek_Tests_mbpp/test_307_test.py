import unittest
from mbpp_307_code import colon_tuplex

class TestColonTuplex(unittest.TestCase):

    def test_typical_case(self):
        tuplex = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
        m = 1
        n = 10
        expected_result = ([1, 2, 3], [4, 10, 5, 6], [7, 8, 9])
        self.assertEqual(colon_tuplex(tuplex, m, n), expected_result)

    def test_edge_case_m_out_of_range(self):
        tuplex = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
        m = 3
        n = 10
        with self.assertRaises(IndexError):
            colon_tuplex(tuplex, m, n)

    def test_edge_case_n_out_of_range(self):
        tuplex = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
        m = 1
        n = 'a'
        with self.assertRaises(TypeError):
            colon_tuplex(tuplex, m, n)

    def test_edge_case_empty_tuplex(self):
        tuplex = ()
        m = 0
        n = 10
        expected_result = ()
        self.assertEqual(colon_tuplex(tuplex, m, n), expected_result)
