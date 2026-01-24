import unittest
from mbpp_298_code import intersection_nested_lists

class TestIntersectionNestedLists(unittest.TestCase):
    def test_intersection_nested_lists(self):
        self.assertEqual(intersection_nested_lists([1, 2, 3], [[1, 2, 3], [4, 5, 6]]), [[1, 2, 3], [1, 2, 3]])
        self.assertEqual(intersection_nested_lists([1, 2, 3], [[1, 2, 3], [4, 5, 7]]), [[1, 2, 3], []])
        self.assertEqual(intersection_nested_lists([1, 2, 3], [[1, 2, 3], [4, 5, 6, 7]]), [[1, 2, 3], []])
        self.assertEqual(intersection_nested_lists([1, 2, 3], [[1, 2, 3], [4, 5, 6, 7, 8]]), [[1, 2, 3], []])
        self.assertEqual(intersection_nested_lists([1, 2, 3], [[1, 2, 3], [4, 5, 6, 7, 8, 9]]), [[1, 2, 3], []])
        self.assertEqual(intersection_nested_lists([1, 2, 3], [[1, 2, 3], [4, 5, 6, 7, 8, 9, 10]]), [[1, 2, 3], []])
        self.assertEqual(intersection_nested_lists([1, 2, 3], [[1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11]]), [[1, 2, 3], []])
        self.assertEqual(intersection_nested_lists([1, 2, 3], [[1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11, 12]]), [[1, 2, 3], []])
        self.assertEqual(intersection_nested_lists([1, 2, 3], [[1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]), [[1, 2, 3], []])
        self.assertEqual(intersection_nested_lists([1, 2, 3], [[1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]), [[1, 2, 3], []])
        self.assertEqual(intersection_nested_lists([1, 2, 3], [[1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]), [[1, 2, 3], []])
        self.assertEqual(intersection_nested_lists([1, 2, 3], [[1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]]), [[1, 2, 3], []])
        self.assertEqual(intersection_nested_lists([1, 2, 3], [[1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]]), [[1, 2, 3], []])
        self.assertEqual(intersection_nested_lists([1, 2, 3], [[1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]]), [[1, 2, 3], []])
        self.assertEqual(intersection_nested_lists([1, 2, 3], [[1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]), [[1, 2, 3], []])
        self.assertEqual(intersection_nested_lists([1, 2, 3], [[1, 2, 3], [