import unittest
from mbpp_111_code import common_in_nested_lists

class TestCommonInNestedLists(unittest.TestCase):

    def test_typical_case(self):
        nestedlist = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        self.assertEqual(common_in_nested_lists(nestedlist), [3])

    def test_single_element(self):
        nestedlist = [[1], [1]]
        self.assertEqual(common_in_nested_lists(nestedlist), [1])

    def test_empty_lists(self):
        nestedlist = [[], []]
        self.assertEqual(common_in_nested_lists(nestedlist), [])

    def test_no_common_elements(self):
        nestedlist = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(common_in_nested_lists(nestedlist), [])

    def test_empty_nested_list(self):
        nestedlist = [[]]
        self.assertEqual(common_in_nested_lists(nestedlist), [])

    def test_none_input(self):
        with self.assertRaises(TypeError):
            common_in_nested_lists(None)

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            common_in_nested_lists(123)

    def test_non_list_elements(self):
        nestedlist = [[1, 2, 3], '2', 3]
        with self.assertRaises(TypeError):
            common_in_nested_lists(nestedlist)
