import unittest
from mbpp_255_code import combinations_colors

class TestCombinationsColors(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual([], combinations_colors([], 3))

    def test_single_element(self):
        self.assertListEqual([('a',)], combinations_colors(['a'], 1))
        self.assertListEqual([('a', 'a'), ('a',)], combinations_colors(['a'], 2))

    def test_multiple_elements(self):
        self.assertListEqual([('a', 'b'), ('a', 'c'), ('b', 'c')], combinations_colors(['a', 'b', 'c'], 2))
        self.assertListEqual([('a', 'b', 'c'), ('a', 'b', 'a'), ('a', 'c', 'a'), ('b', 'a', 'a'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('a', 'a', 'b'), ('a', 'a', 'c'), ('a', 'b', 'b'), ('a', 'b', 'c'), ('a', 'c', 'c'), ('b', 'a', 'b'), ('b', 'c', 'b'), ('c', 'a', 'c'), ('c', 'b', 'c')], combinations_colors(['a', 'b', 'c'], 3))

    def test_negative_n(self):
        with self.assertRaises(ValueError):
            combinations_colors(['a', 'b', 'c'], -1)

    def test_zero_n(self):
        self.assertListEqual([], combinations_colors(['a', 'b', 'c'], 0))
