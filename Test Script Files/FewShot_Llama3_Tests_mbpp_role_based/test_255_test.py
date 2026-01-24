import unittest
from mbpp_255_code import combinations_colors

class TestCombinationsColors(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(combinations_colors([], 3), [])

    def test_single_element_list(self):
        self.assertEqual(combinations_colors(['a'], 3), [['a', 'a', 'a'], ['a', 'a', 'a'], ['a', 'a', 'a']])

    def test_multiple_elements_list(self):
        self.assertEqual(combinations_colors(['a', 'b', 'c'], 2), [['a', 'a'], ['a', 'b'], ['a', 'c'], ['b', 'b'], ['b', 'c'], ['c', 'c']])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            combinations_colors('abc', 3)

    def test_invalid_input_value(self):
        with self.assertRaises(ValueError):
            combinations_colors([1, 2, 3], -1)
