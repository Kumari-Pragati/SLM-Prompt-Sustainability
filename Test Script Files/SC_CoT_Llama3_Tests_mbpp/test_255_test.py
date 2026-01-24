import unittest
from mbpp_255_code import combinations_colors

class TestCombinationsColors(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(combinations_colors(['a', 'b', 'c'], 2), 
                         [[('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'b'), ('b', 'c'), ('c', 'c')], 
                          [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'b'), ('b', 'c'), ('c', 'c')], 
                          [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'b'), ('b', 'c'), ('c', 'c')]])

    def test_edge_case_n_zero(self):
        self.assertEqual(combinations_colors(['a', 'b', 'c'], 0), [])

    def test_edge_case_n_one(self):
        self.assertEqual(combinations_colors(['a', 'b', 'c'], 1), 
                         [[('a',), ('b',), ('c',)], [('a',), ('b',), ('c',)], [('a',), ('b',), ('c',)]])

    def test_edge_case_n_equal_to_length(self):
        self.assertEqual(combinations_colors(['a', 'b', 'c'], 3), 
                         [[('a', 'a', 'a'), ('a', 'a', 'b'), ('a', 'a', 'c'), ('a', 'b', 'b'), ('a', 'b', 'c'), 
                          ('a', 'c', 'c'), ('b', 'b', 'b'), ('b', 'b', 'c'), ('b', 'c', 'c'), ('c', 'c', 'c')], 
                          [('a', 'a', 'a'), ('a', 'a', 'b'), ('a', 'a', 'c'), ('a', 'b', 'b'), ('a', 'b', 'c'), 
                          ('a', 'c', 'c'), ('b', 'b', 'b'), ('b', 'b', 'c'), ('b', 'c', 'c'), ('c', 'c', 'c')], 
                          [('a', 'a', 'a'), ('a', 'a', 'b'), ('a', 'a', 'c'), ('a', 'b', 'b'), ('a', 'b', 'c'), 
                          ('a', 'c', 'c'), ('b', 'b', 'b'), ('b', 'b', 'c'), ('b', 'c', 'c'), ('c', 'c', 'c')]])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            combinations_colors(123, 2)

    def test_invalid_input_non_positive_n(self):
        with self.assertRaises(TypeError):
            combinations_colors(['a', 'b', 'c'], -1)

    def test_invalid_input_non_list_and_non_positive_n(self):
        with self.assertRaises(TypeError):
            combinations_colors(123, -1)
