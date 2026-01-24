import unittest
from mbpp_255_code import combinations_colors

class TestCombinationsColors(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(combinations_colors(['A', 'B', 'C'], 1), [['A'], ['B'], ['C']])
        self.assertEqual(combinations_colors(['A', 'B', 'C'], 2), [['A', 'A'], ['A', 'B'], ['A', 'C'], ['B', 'B'], ['B', 'C'], ['C', 'C']])

    def test_edge_cases(self):
        self.assertEqual(combinations_colors([], 1), [])
        self.assertEqual(combinations_colors(['A'], 2), [['A', 'A']])
        self.assertEqual(combinations_colors(['A', 'B'], 0), [])
        self.assertEqual(combinations_colors(['A', 'B'], 3), [['A', 'A', 'A'], ['A', 'A', 'B'], ['A', 'B', 'B'], ['B', 'B', 'B']])

    def test_complex(self):
        self.assertEqual(combinations_colors(['A', 'B', 'C', 'D'], 2), [['A', 'A'], ['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'B'], ['B', 'C'], ['B', 'D'], ['C', 'C'], ['C', 'D'], ['D', 'D']])
        self.assertEqual(combinations_colors(['A', 'B', 'C', 'D', 'E'], 3), [['A', 'A', 'A'], ['A', 'A', 'B'], ['A', 'A', 'C'], ['A', 'A', 'D'], ['A', 'A', 'E'], ['A', 'B', 'B'], ['A', 'B', 'C'], ['A', 'B', 'D'], ['A', 'B', 'E'], ['A', 'C', 'C'], ['A', 'C', 'D'], ['A', 'C', 'E'], ['A', 'D', 'D'], ['A', 'D', 'E'], ['A', 'E', 'E'], ['B', 'B', 'B'], ['B', 'B', 'C'], ['B', 'B', 'D'], ['B', 'B', 'E'], ['B', 'C', 'C'], ['B', 'C', 'D'], ['B', 'C', 'E'], ['B', 'D', 'D'], ['B', 'D', 'E'], ['B', 'E', 'E'], ['C', 'C', 'C'], ['C', 'C', 'D'], ['C', 'C', 'E'], ['C', 'D', 'D'], ['C', 'D', 'E'], ['C', 'E', 'E'], ['D', 'D', 'D'], ['D', 'D', 'E'], ['D', 'E', 'E'], ['E', 'E', 'E']])
