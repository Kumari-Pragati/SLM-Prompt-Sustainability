import unittest
from mbpp_298_code import intersection_nested_lists

class TestIntersectionNestedLists(unittest.TestCase):
    def test_empty_lists(self):
        l1 = []
        l2 = []
        self.assertEqual(intersection_nested_lists(l1, l2), [])

    def test_single_element_lists(self):
        l1 = [1]
        l2 = [[1]]
        self.assertEqual(intersection_nested_lists(l1, l2), [[1]])

    def test_multiple_element_lists(self):
        l1 = [1, 2, 3]
        l2 = [[1, 2], [2, 3], [3, 1]]
        self.assertEqual(intersection_nested_lists(l1, l2), [[1, 2], [2, 3], [3, 1]])

    def test_lists_with_duplicates(self):
        l1 = [1, 2, 2]
        l2 = [[1, 2, 2], [2, 2, 3]]
        self.assertEqual(intersection_nested_lists(l1, l2), [[1, 2, 2], [2, 2]])

    def test_lists_with_empty_sublists(self):
        l1 = [1, 2]
        l2 = [[], [1, 2], [2, 3]]
        self.assertEqual(intersection_nested_lists(l1, l2), [[1, 2]])

    def test_lists_with_non_list_elements(self):
        l1 = [1, 2]
        l2 = [[1, 2], 'hello', [3, 4]]
        with self.assertRaises(TypeError):
            intersection_nested_lists(l1, l2)
