import unittest
from mbpp_298_code import intersection_nested_lists

class TestIntersectionNestedLists(unittest.TestCase):

    def test_intersection_nested_lists_typical(self):
        l1 = [1, 2, 3]
        l2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(intersection_nested_lists(l1, l2), [[1, 2, 3], [], []])

    def test_intersection_nested_lists_edge_case1(self):
        l1 = [1, 2, 3]
        l2 = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(intersection_nested_lists(l1, l2), [[1, 2, 3], []])

    def test_intersection_nested_lists_edge_case2(self):
        l1 = [1, 2, 3]
        l2 = [[1, 2, 3], [1, 2, 3]]
        self.assertEqual(intersection_nested_lists(l1, l2), [[1, 2, 3], [1, 2, 3]])

    def test_intersection_nested_lists_edge_case3(self):
        l1 = [1, 2, 3]
        l2 = [[], [1, 2, 3]]
        self.assertEqual(intersection_nested_lists(l1, l2), [[], [1, 2, 3]])

    def test_intersection_nested_lists_edge_case4(self):
        l1 = [1, 2, 3]
        l2 = [[], []]
        self.assertEqual(intersection_nested_lists(l1, l2), [[], []])

    def test_intersection_nested_lists_invalid_input1(self):
        l1 = [1, 2, 3]
        l2 = 'not a list'
        with self.assertRaises(TypeError):
            intersection_nested_lists(l1, l2)

    def test_intersection_nested_lists_invalid_input2(self):
        l1 = 'not a list'
        l2 = [[1, 2, 3], [4, 5, 6]]
        with self.assertRaises(TypeError):
            intersection_nested_lists(l1, l2)

    def test_intersection_nested_lists_invalid_input3(self):
        l1 = [1, 2, 3]
        l2 = [[1, 2, 3], [4, 5, 6]]
        with self.assertRaises(TypeError):
            intersection_nested_lists(l1, None)

    def test_intersection_nested_lists_invalid_input4(self):
        l1 = None
        l2 = [[1, 2, 3], [4, 5, 6]]
        with self.assertRaises(TypeError):
            intersection_nested_lists(l1, l2)
