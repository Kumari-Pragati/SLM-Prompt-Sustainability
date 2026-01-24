import unittest
from mbpp_255_code import combinations_colors

class TestCombinationsColors(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(combinations_colors([], 1), [])

    def test_single_element_list(self):
        self.assertEqual(combinations_colors(['a'], 1), [['a']])

    def test_multiple_elements_list(self):
        self.assertEqual(combinations_colors(['a', 'b', 'c'], 2), [['a', 'a'], ['a', 'b'], ['a', 'c'], ['b', 'b'], ['b', 'c'], ['c', 'c']])

    def test_large_list(self):
        self.assertEqual(combinations_colors(['a', 'b', 'c', 'd', 'e'], 3), [['a', 'a', 'a'], ['a', 'a', 'b'], ['a', 'a', 'c'], ['a', 'a', 'd'], ['a', 'a', 'e'], ['a', 'b', 'b'], ['a', 'b', 'c'], ['a', 'b', 'd'], ['a', 'b', 'e'], ['a', 'c', 'c'], ['a', 'c', 'd'], ['a', 'c', 'e'], ['a', 'd', 'd'], ['a', 'd', 'e'], ['a', 'e', 'e'], ['b', 'b', 'b'], ['b', 'b', 'c'], ['b', 'b', 'd'], ['b', 'b', 'e'], ['b', 'c', 'c'], ['b', 'c', 'd'], ['b', 'c', 'e'], ['b', 'd', 'd'], ['b', 'd', 'e'], ['b', 'e', 'e'], ['c', 'c', 'c'], ['c', 'c', 'd'], ['c', 'c', 'e'], ['c', 'd', 'd'], ['c', 'd', 'e'], ['c', 'e', 'e'], ['d', 'd', 'd'], ['d', 'd', 'e'], ['d', 'e', 'e'], ['e', 'e', 'e']])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            combinations_colors('a', 1)

    def test_invalid_input_value(self):
        with self.assertRaises(TypeError):
            combinations_colors([1, 2, 3], 'a')
