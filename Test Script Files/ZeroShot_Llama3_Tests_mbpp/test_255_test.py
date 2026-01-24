import unittest
from mbpp_255_code import combinations_colors

class TestCombinationsColors(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(combinations_colors([], 0), [])

    def test_single_element_list(self):
        self.assertEqual(combinations_colors(['a'], 0), [[]])
        self.assertEqual(combinations_colors(['a'], 1), [['a']])

    def test_multiple_elements_list(self):
        self.assertEqual(combinations_colors(['a', 'b', 'c'], 0), [[]])
        self.assertEqual(combinations_colors(['a', 'b', 'c'], 1, ['a', 'b', 'c']), [['a'], ['b'], ['c']])
        self.assertEqual(combinations_colors(['a', 'b', 'c'], 2, ['a', 'b', 'c']), [['a', 'a'], ['a', 'b'], ['a', 'c'], ['b', 'b'], ['b', 'c'], ['c', 'c']])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            combinations_colors('a', 1)
        with self.assertRaises(TypeError):
            combinations_colors([1, 2, 3], 'a')
