import unittest
from mbpp_298_code import intersection_nested_lists

class TestIntersectionNestedLists(unittest.TestCase):

    def test_typical_case(self):
        l1 = [1, 2, 3, 4]
        l2 = [[1, 2], [3, 4], [5, 6]]
        expected_output = [[1, 2], [3, 4], []]
        self.assertEqual(intersection_nested_lists(l1, l2), expected_output)

    def test_empty_lists(self):
        l1 = []
        l2 = [[1, 2], [3, 4], [5, 6]]
        expected_output = [[] for _ in l2]
        self.assertEqual(intersection_nested_lists(l1, l2), expected_output)

    def test_single_element_lists(self):
        l1 = [1]
        l2 = [[1, 2], [3, 4], [5, 6]]
        expected_output = [[1], [], []]
        self.assertEqual(intersection_nested_lists(l1, l2), expected_output)

    def test_no_intersection(self):
        l1 = [1, 2, 3, 4]
        l2 = [[5, 6], [7, 8], [9, 10]]
        expected_output = [[], [], []]
        self.assertEqual(intersection_nested_lists(l1, l2), expected_output)

    def test_same_elements(self):
        l1 = [1, 2, 3, 4]
        l2 = [[1, 1], [2, 2], [3, 3], [4, 4]]
        expected_output = [[1, 1], [2, 2], [3, 3], [4, 4]]
        self.assertEqual(intersection_nested_lists(l1, l2), expected_output)

    def test_invalid_input(self):
        l1 = [1, 2, 3, 4]
        l2 = [1, 2, 3, 4]
        with self.assertRaises(TypeError):
            intersection_nested_lists(l1, l2)
