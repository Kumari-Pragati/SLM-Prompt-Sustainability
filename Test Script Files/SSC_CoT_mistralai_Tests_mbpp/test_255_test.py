import unittest
from mbpp_255_code import combinations_with_replacement
from 255_code import combinations_colors

class TestCombinationsColors(unittest.TestCase):

    def test_normal(self):
        self.assertListEqual(combinations_colors(['R', 'G', 'B'], 2), [['R', 'R'], ['R', 'G'], ['R', 'B'], ['G', 'G'], ['G', 'R'], ['G', 'B'], ['B', 'B'], ['B', 'R'], ['B', 'G']])
        self.assertListEqual(combinations_colors(['A', 'B', 'C', 'D'], 3), [['A', 'A', 'A'], ['A', 'A', 'B'], ['A', 'A', 'C'], ['A', 'A', 'D'], ['A', 'B', 'B'], ['A', 'B', 'C'], ['A', 'B', 'D'], ['A', 'C', 'C'], ['A', 'C', 'D'], ['A', 'D', 'D'], ['B', 'B', 'B'], ['B', 'B', 'C'], ['B', 'B', 'D'], ['B', 'C', 'C'], ['B', 'C', 'D'], ['B', 'D', 'D'], ['C', 'C', 'C'], ['C', 'C', 'D'], ['C', 'D', 'D'], ['D', 'D', 'D']])

    def test_edge_and_boundary(self):
        self.assertListEqual(combinations_colors(['R', 'G', 'B'], 0), [])
        self.assertListEqual(combinations_colors(['R', 'G', 'B'], 4), [['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'G'], ['R', 'R', 'R', 'B'], ['R', 'R', 'G', 'G'], ['R', 'R', 'G', 'B'], ['R', 'R', 'B', 'B'], ['R', 'G', 'G', 'G'], ['R', 'G', 'G', 'B'], ['R', 'G', 'B', 'B'], ['R', 'B', 'B', 'B'], ['G', 'G', 'G', 'G'], ['G', 'G', 'G', 'B'], ['G', 'G', 'B', 'B'], ['G', 'B', 'B', 'B'], ['B', 'B', 'B', 'B']])
        self.assertListEqual(combinations_colors([], 2), [])
        self.assertListEqual(combinations_colors(['R'], 2), [['R', 'R']])

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            combinations_colors('ABC', 5)
        with self.assertRaises(ValueError):
            combinations_colors(['A', 'B', 'C'], -1)
        with self.assertRaises(ValueError):
            combinations_colors(['A', 'B', 'C'], 0)
        with self.assertRaises(ValueError):
            combinations_colors([], 2)
