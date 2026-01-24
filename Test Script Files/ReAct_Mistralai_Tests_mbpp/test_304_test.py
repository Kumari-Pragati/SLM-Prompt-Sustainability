import unittest
from mbpp_304_code import find_Element

class TestFindElement(unittest.TestCase):

    def test_find_element_within_range(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        ranges = [[0, 2], [3, 5], [6, 8]]
        rotations = 2
        index = 3
        self.assertEqual(find_Element(arr, ranges, rotations, index), 5)

    def test_find_element_at_left_edge(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        ranges = [[0, 1], [3, 5], [6, 8]]
        rotations = 2
        index = 0
        self.assertEqual(find_Element(arr, ranges, rotations, index), 1)

    def test_find_element_at_right_edge(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        ranges = [[0, 2], [3, 6], [6, 8]]
        rotations = 2
        index = 7
        self.assertEqual(find_Element(arr, ranges, rotations, index), 7)

    def test_find_element_outside_range(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        ranges = [[0, 2], [3, 5], [6, 8]]
        rotations = 2
        index = 8
        self.assertRaises(IndexError, find_Element, arr, ranges, rotations, index)

    def test_find_element_with_empty_ranges(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        ranges = []
        rotations = 2
        index = 3
        self.assertRaises(ValueError, find_Element, arr, ranges, rotations, index)

    def test_find_element_with_negative_rotations(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        ranges = [[0, 2], [3, 5], [6, 8]]
        rotations = -1
        index = 3
        self.assertRaises(ValueError, find_Element, arr, ranges, rotations, index)
