import unittest
from mbpp_255_code import combinations_colors

class TestCombinationsColors(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(combinations_colors([], 1), [])

    def test_single_element(self):
        self.assertListEqual(combinations_colors(['A'], 1), ['A'])
        self.assertListEqual(combinations_colors(['A'], 2), [['A'], ['A']])

    def test_multiple_elements(self):
        self.assertListEqual(combinations_colors(['A', 'B'], 1), ['A', 'B'])
        self.assertListEqual(combinations_colors(['A', 'B'], 2), [['A', 'A'], ['A', 'B'], ['B', 'A'], ['B', 'B']])
        self.assertListEqual(combinations_colors(['A', 'B'], 3), [['A', 'A', 'A'], ['A', 'A', 'B'], ['A', 'B', 'A'], ['A', 'B', 'B'], ['B', 'A', 'A'], ['B', 'A', 'B'], ['B', 'B', 'A'], ['B', 'B', 'B']])

    def test_negative_n(self):
        with self.assertRaises(ValueError):
            combinations_colors(['A', 'B'], -1)
