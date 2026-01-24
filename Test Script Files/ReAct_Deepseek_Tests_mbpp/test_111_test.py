import unittest
from mbpp_111_code import common_in_nested_lists

class TestCommonInNestedLists(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5]]), [3])

    def test_empty_nested_list(self):
        self.assertEqual(common_in_nested_lists([[], []]), [])

    def test_single_element_in_nested_list(self):
        self.assertEqual(common_in_nested_lists([[1], [1]]), [1])

    def test_no_common_elements(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [4, 5, 6]]), [])

    def test_duplicate_common_elements(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 2], [2, 2, 3]]), [2])

    def test_non_integer_elements(self):
        self.assertEqual(common_in_nested_lists([['a', 'b', 'c'], ['b', 'c', 'd']]), ['c'])

    def test_large_input(self):
        large_list = [[i for i in range(1, 1000)] for _ in range(10)]
        self.assertEqual(common_in_nested_lists(large_list), list(range(1, 1000)))

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            common_in_nested_lists(123)
        with self.assertRaises(TypeError):
            common_in_nested_lists([1, 2, 3])
        with self.assertRaises(TypeError):
            common_in_nested_lists([[], 1])
