import unittest
from mbpp_298_code import intersection_nested_lists

class TestIntersectionNestedLists(unittest.TestCase):
    def test_simple_intersection(self):
        l1 = [1, 2, 3]
        l2 = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(intersection_nested_lists(l1, l2), [[1, 2, 3], [1, 2, 3]])

    def test_empty_lists(self):
        l1 = []
        l2 = []
        self.assertEqual(intersection_nested_lists(l1, l2), [])

    def test_empty_l1(self):
        l1 = []
        l2 = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(intersection_nested_lists(l1, l2), [])

    def test_empty_l2(self):
        l1 = [1, 2, 3]
        l2 = []
        self.assertEqual(intersection_nested_lists(l1, l2), [])

    def test_single_element_l1(self):
        l1 = [1]
        l2 = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(intersection_nested_lists(l1, l2), [[1], [1]])

    def test_single_element_l2(self):
        l1 = [1, 2, 3]
        l2 = [[1]]
        self.assertEqual(intersection_nested_lists(l1, l2), [[1]])

    def test_multiple_elements_l1(self):
        l1 = [1, 2, 3]
        l2 = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(intersection_nested_lists(l1, l2), [[1, 2, 3], [1, 2, 3]])

    def test_multiple_elements_l2(self):
        l1 = [1, 2, 3]
        l2 = [[1, 2], [3, 4, 5]]
        self.assertEqual(intersection_nested_lists(l1, l2), [[1, 2], [1, 2]])

    def test_non_intersecting_lists(self):
        l1 = [1, 2, 3]
        l2 = [[4, 5, 6], [7, 8, 9]]
        self.assertEqual(intersection_nested_lists(l1, l2), [[], []])
