import unittest
from mbpp_298_code import intersection_nested_lists

class TestIntersectionNestedLists(unittest.TestCase):

    def test_empty_lists(self):
        self.assertListEqual(intersection_nested_lists([], []), [])

    def test_single_list(self):
        self.assertListEqual(intersection_nested_lists([1, 2, 3], [[1], [2, 3], [4]]), [[1]])

    def test_simple_intersection(self):
        self.assertListEqual(intersection_nested_lists([1, 2, 3], [[1, 2], [2, 3], [3, 4]]), [[2]])

    def test_complex_intersection(self):
        self.assertListEqual(intersection_nested_lists(
            [['a', 1], ['b', 2], ['c', 3]],
            [['a', 'b'], [1, 2, 3], ['b', 2, 4]]
        ), [['b', 2]])

    def test_no_intersection(self):
        self.assertListEqual(intersection_nested_lists([1, 2, 3], [[4, 5, 6], [7, 8, 9]]), [])
