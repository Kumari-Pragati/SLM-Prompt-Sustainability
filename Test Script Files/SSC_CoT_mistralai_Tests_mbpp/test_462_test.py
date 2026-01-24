import unittest
from mbpp_462_code import combinations_list

class TestCombinationsList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(combinations_list([]), [[]])

    def test_single_element_list(self):
        self.assertEqual(combinations_list([1]), [[1]])

    def test_normal_list(self):
        self.assertEqual(combinations_list([1, 2]), [[1], [2], [1, 2]])
        self.assertEqual(combinations_list([1, 2, 3]), [[1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])

    def test_edge_cases(self):
        self.assertEqual(combinations_list([1, 2, 3, 4]), [
            [1], [2], [3], [4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4],
            [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]
        ])
        self.assertEqual(combinations_list([1, 2, 3, 4, 5]), [
            [1], [2], [3], [4], [5], [1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5],
            [1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5],
            [1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 4, 5], [1, 3, 4, 5], [2, 3, 4, 5]
        ])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            combinations_list(123)
