import unittest
from mbpp_255_code import combinations_colors

class TestCombinationsColors(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(combinations_colors([], 0), [])

    def test_single_element(self):
        self.assertEqual(combinations_colors(['a'], 0), [[]])
        self.assertEqual(combinations_colors(['a'], 1), ['a'])
        self.assertEqual(combinations_colors(['a'], 2, ), ['aa'])

    def test_multiple_elements(self):
        self.assertEqual(combinations_colors(['a', 'b'], 0), [[]])
        self.assertEqual(combinations_colors(['a', 'b'], 1, ), ['a', 'b'])
        self.assertEqual(combinations_colors(['a', 'b'], 2, ), ['aa', 'ab', 'ba', 'bb'])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            combinations_colors(None, 0)
        with self.assertRaises(TypeError):
            combinations_colors([], 'a')
