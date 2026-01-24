import unittest
from mbpp_111_code import common_in_nested_lists

class TestCommonInNestedLists(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(common_in_nested_lists([]), [])

    def test_single_element_input(self):
        self.assertEqual(common_in_nested_lists([[1]]), [1])

    def test_multiple_elements_input(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4]]), [2, 3])

    def test_duplicates_input(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 2, 3], [2, 3, 3, 4]]), [2, 3])

    def test_empty_sublists_input(self):
        self.assertEqual(common_in_nested_lists([[1, 2], [], [3, 4]]), [1, 2, 3, 4])

    def test_negative_numbers_input(self):
        self.assertEqual(common_in_nested_lists([[-1, 2, 3], [2, 3, 4]]), [2, 3])

    def test_non_integer_input(self):
        self.assertEqual(common_in_nested_lists([['a', 'b', 'c'], ['b', 'c', 'd']]), ['b', 'c'])
