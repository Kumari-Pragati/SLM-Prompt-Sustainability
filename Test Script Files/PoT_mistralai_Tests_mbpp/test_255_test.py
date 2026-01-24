import unittest
from mbpp_255_code import combinations_colors

class TestCombinationsColors(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(combinations_colors(['A', 'B', 'C'], 2), [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')])
        self.assertEqual(combinations_colors(['a', 'b', 'c'], 3), [('a', 'a', 'a'), ('a', 'a', 'b'), ('a', 'a', 'c'), ('a', 'b', 'b'), ('a', 'b', 'c'), ('a', 'c', 'c'), ('b', 'b', 'b'), ('b', 'b', 'c'), ('b', 'c', 'c'), ('c', 'c', 'c')])

    def test_edge_case_empty_list(self):
        self.assertEqual(combinations_colors([], 2), [])

    def test_edge_case_single_element(self):
        self.assertEqual(combinations_colors(['A'], 2), [('A', 'A')])

    def test_edge_case_single_element_n_greater_than_1(self):
        self.assertEqual(combinations_colors(['A'], 3), [('A', 'A', 'A')])

    def test_edge_case_n_greater_than_len_list(self):
        self.assertEqual(combinations_colors(['A', 'B'], 4), [('A', 'A', 'A', 'A'), ('A', 'A', 'A', 'B'), ('A', 'A', 'B', 'B'), ('A', 'B', 'B', 'B')])
