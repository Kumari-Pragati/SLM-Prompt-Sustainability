import unittest
from mbpp_307_code import colon_tuplex

class TestColonTuplex(unittest.TestCase):
    def test_typical_case(self):
        tuplex = ([1, 2, 3], [4, 5, 6])
        m = 0
        n = 7
        expected = ([1, 2, 3], [4, 5, 6], [7])
        self.assertEqual(colon_tuplex(tuplex, m, n), expected)

    def test_edge_case_m_out_of_range(self):
        tuplex = ([1, 2, 3], [4, 5, 6])
        m = 1
        n = 7
        expected = ([1, 2, 3], [4, 5, 6, [7]])
        self.assertEqual(colon_tuplex(tuplex, m, n), expected)

    def test_edge_case_m_zero(self):
        tuplex = ([1, 2, 3], [4, 5, 6])
        m = 0
        n = 7
        expected = ([1, 2, 3], [4, 5, 6, [7]])
        self.assertEqual(colon_tuplex(tuplex, m, n), expected)

    def test_edge_case_m_greater_than_length(self):
        tuplex = ([1, 2, 3], [4, 5, 6])
        m = 2
        n = 7
        expected = ([1, 2, 3], [4, 5, 6], [7])
        self.assertEqual(colon_tuplex(tuplex, m, n), expected)

    def test_invalid_input_type_m(self):
        tuplex = ([1, 2, 3], [4, 5, 6])
        m = 'a'
        n = 7
        with self.assertRaises(TypeError):
            colon_tuplex(tuplex, m, n)

    def test_invalid_input_type_n(self):
        tuplex = ([1, 2, 3], [4, 5, 6])
        m = 0
        n = 'b'
        with self.assertRaises(TypeError):
            colon_tuplex(tuplex, m, n)
