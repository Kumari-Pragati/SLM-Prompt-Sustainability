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

    def test_four_elements_list(self):
        self.assertEqual(combinations_list([1, 2, 3, 4]),
                         [[1], [2], [3], [4], [1, 2], [1, 3], [1, 4],
                          [2, 3], [2, 4], [3, 4], [1, 2, 3], [1, 2, 4],
                          [1, 3, 4], [2, 3, 4]])

    def test_negative_elements_list(self):
        self.assertEqual(combinations_list([-1, 2, 3]),
                         [[-1], [2], [3], [-1, 2], [-1, 3], [2, 3]])

    def test_mixed_elements_list(self):
        self.assertEqual(combinations_list([1, -1, 2, 3]),
                         [[1], [-1], [2], [3], [1, -1], [1, 2], [1, 3],
                          [-1, 2], [-1, 3], [2, 3]])
