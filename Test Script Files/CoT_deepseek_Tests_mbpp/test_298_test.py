import unittest
from mbpp_298_code import intersection_nested_lists

class TestIntersectionNestedLists(unittest.TestCase):

    def test_typical_case(self):
        l1 = [1, 2, 3]
        l2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_output = [[1, 2, 3], [], []]
        self.assertEqual(intersection_nested_lists(l1, l2), expected_output)

    def test_empty_lists(self):
        l1 = []
        l2 = [[]]
        expected_output = [[]]
        self.assertEqual(intersection_nested_lists(l1, l2), expected_output)

    def test_no_intersection(self):
        l1 = [1, 2, 3]
        l2 = [[4, 5, 6], [7, 8, 9]]
        expected_output = [[], []]
        self.assertEqual(intersection_nested_lists(l1, l2), expected_output)

    def test_single_element(self):
        l1 = [1]
        l2 = [[1], [2, 3]]
        expected_output = [[1], []]
        self.assertEqual(intersection_nested_lists(l1, l2), expected_output)

    def test_duplicate_elements(self):
        l1 = [1, 1]
        l2 = [[1, 1], [2, 2]]
        expected_output = [[1, 1], []]
        self.assertEqual(intersection_nested_lists(l1, l2), expected_output)

    def test_invalid_input(self):
        l1 = [1, 2, 3]
        l2 = "not a list"
        with self.assertRaises(TypeError):
            intersection_nested_lists(l1, l2)
