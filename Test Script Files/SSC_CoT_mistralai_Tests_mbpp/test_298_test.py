import unittest
from mbpp_298_code import deepcopy
from 298_code import intersection_nested_lists

class TestIntersectionNestedLists(unittest.TestCase):

    def test_normal_case(self):
        l1 = [1, 2, 3, [4, 5], [6, 7, 8]]
        l2 = [[1, 2], [3], [4, 5], [6, 7, 8]]
        expected = [[1, 2], [], [4, 5], [6, 7, 8]]
        self.assertEqual(intersection_nested_lists(l1, l2), expected)

    def test_empty_lists(self):
        self.assertEqual(intersection_nested_lists([], []), [])

    def test_single_list(self):
        l1 = [1, 2, 3]
        l2 = [[1], [2], [3]]
        expected = [[1], [2], [3]]
        self.assertEqual(intersection_nested_lists(l1, l2), expected)

    def test_single_element_lists(self):
        l1 = [1]
        l2 = [[1]]
        expected = [[1]]
        self.assertEqual(intersection_nested_lists(l1, l2), expected)

    def test_no_intersection(self):
        l1 = [1, 2, 3]
        l2 = [[4, 5], [6, 7], [8, 9]]
        expected = []
        self.assertEqual(intersection_nested_lists(l1, l2), expected)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            intersection_nested_lists('list1', [1, 2, 3])
        with self.assertRaises(TypeError):
            intersection_nested_lists([1, 2, 3], 'list2')
        with self.assertRaises(TypeError):
            intersection_nested_lists([1, 2, 3], 2)
        with self.assertRaises(TypeError):
            intersection_nested_lists(1, [1, 2, 3])
