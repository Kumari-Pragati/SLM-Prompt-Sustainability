import unittest
from mbpp_462_code import combinations_list

class TestCombinationsList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(combinations_list([]), [[]])

    def test_single_element_list(self):
        self.assertEqual(combinations_list([1]), [[1]])

    def test_multiple_elements_list(self):
        self.assertEqual(combinations_list([1, 2]), [[1], [2], [1, 2]])

    def test_list_with_duplicates(self):
        self.assertEqual(combinations_list([1, 1, 2]), [[1], [1, 1], [2]])

    def test_list_with_long_elements(self):
        self.assertEqual(combinations_list([[1], [2]]), [[], [1], [2], [1, 2]])
