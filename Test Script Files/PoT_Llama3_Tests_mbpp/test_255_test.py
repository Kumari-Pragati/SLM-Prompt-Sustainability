import unittest
from mbpp_255_code import combinations_colors

class TestCombinationsColors(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(combinations_colors([1, 2, 3], 2), [[1, 1], [1, 2], [1, 3], [2, 2], [2, 3], [3, 3]])

    def test_edge_case(self):
        self.assertEqual(combinations_colors([1, 2, 3], 0), [])

    def test_edge_case2(self):
        self.assertEqual(combinations_colors([1, 2, 3], 3), [[1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 2, 2], [1, 2, 3], [1, 3, 3], [2, 2, 2], [2, 2, 3], [2, 3, 3], [3, 3, 3]])

    def test_edge_case3(self):
        self.assertEqual(combinations_colors([], 2), [])

    def test_edge_case4(self):
        self.assertEqual(combinations_colors([1], 2), [[1, 1]])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            combinations_colors('abc', 2)
