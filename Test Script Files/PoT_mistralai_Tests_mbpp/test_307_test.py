import unittest
from mbpp_307_code import deepcopy
from 307_code import colon_tuplex

class TestColonTuplex(unittest.TestCase):

    def test_typical_case(self):
        data = [(1, [1, 2, 3]), (2, [4, 5]), (3, [6])]
        for tuplex, m, n in data:
            result = colon_tuplex(tuplex, m, n)
            self.assertEqual(result, [(1, [1, 2, 3]), (2, [4, 5, n]), (3, [6, m])])

    def test_edge_case_empty_list(self):
        self.assertEqual(colon_tuplex([], 1, 2), [(1, [2])])

    def test_edge_case_single_element_list(self):
        self.assertEqual(colon_tuplex((1,), 1, 2), [(1, [2])])

    def test_edge_case_m_greater_than_length(self):
        self.assertEqual(colon_tuplex([(1, [1, 2, 3]), (2, [4, 5])], 3, 2), [(1, [1, 2, 3]), (2, [4, 5, 2])])

    def test_edge_case_m_equal_to_length(self):
        self.assertEqual(colon_tuplex([(1, [1, 2, 3]), (2, [4, 5])], 2, 2), [(1, [1, 2, 3, 2]), (2, [4, 5, 2])])

    def test_edge_case_negative_m(self):
        self.assertEqual(colon_tuplex([(1, [1, 2, 3]), (2, [4, 5])], -1, 2), [(1, [1, 2, 3]), (2, [4, 5, 2])])

    def test_edge_case_m_zero(self):
        self.assertEqual(colon_tuplex([(1, [1, 2, 3]), (2, [4, 5])], 0, 2), [(1, [1, 2, 3]), (2, [4, 5, 2])])
