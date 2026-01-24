import unittest
from mbpp_462_code import combinations_list

class TestCombinationsList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(combinations_list([]), [[]])

    def test_single_element_list(self):
        self.assertEqual(combinations_list([1]), [[1]])

    def test_two_elements_list(self):
        self.assertEqual(combinations_list([1, 2]), [[1], [2], [1, 2]])

    def test_three_elements_list(self):
        self.assertEqual(combinations_list([1, 2, 3]),
                         [[1], [2], [3], [1, 2], [1, 3], [2, 3]])

    def test_longer_list(self):
        self.assertEqual(combinations_list([1, 2, 3, 4, 5]),
                         [[1], [2], [3], [4], [5], [1, 2], [1, 3], [1, 4], [1, 5],
                          [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]])

    def test_negative_numbers(self):
        self.assertEqual(combinations_list([-1, 2, 3]),
                         [[-1], [2], [3], [-1, 2], [-1, 3], [2, 3]])

    def test_mixed_numbers(self):
        self.assertEqual(combinations_list([-1, 0, 2, 3]),
                         [[-1], [0], [2], [3], [-1, 0], [-1, 2], [-1, 3],
                          [0, 2], [0, 3], [2, 3]])
