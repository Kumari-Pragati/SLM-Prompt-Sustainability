import unittest
from mbpp_255_code import combinations_colors

class TestCombinationsColors(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(combinations_colors([], 0), [])

    def test_single_element_list(self):
        self.assertEqual(combinations_colors([1], 0), [[]])
        self.assertEqual(combinations_colors([1], 1), [[1]])

    def test_single_element_list_with_replacement(self):
        self.assertEqual(combinations_colors([1], 2), [[1, 1], [1]])

    def test_multiple_elements_list(self):
        self.assertEqual(combinations_colors([1, 2, 3], 0), [[]])
        self.assertEqual(combinations_colors([1, 2, 3], 1), [[1], [2], [3]])
        self.assertEqual(combinations_colors([1, 2, 3], 2), [[1, 1], [1, 2], [1, 3], [2, 2], [2, 3], [3, 3]])

    def test_multiple_elements_list_with_replacement(self):
        self.assertEqual(combinations_colors([1, 2, 3], 3), [[1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 2, 2], [1, 2, 3], [1, 3, 3], [2, 2, 2], [2, 2, 3], [2, 3, 3], [3, 3, 3]])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            combinations_colors('abc', 1)

    def test_invalid_input_value(self):
        with self.assertRaises(TypeError):
            combinations_colors([1, 2, 3], 'abc')
