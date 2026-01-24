import unittest
from mbpp_304_code import find_Element

class TestFindElement(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 2
        index = 3
        self.assertEqual(find_Element(arr, ranges, rotations, index), 4)

    def test_edge_case_index_at_left_range(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 2
        index = 1
        self.assertEqual(find_Element(arr, ranges, rotations, index), 2)

    def test_edge_case_index_at_right_range(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 2
        index = 4
        self.assertEqual(find_Element(arr, ranges, rotations, index), 5)

    def test_edge_case_index_at_range_boundary(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 2
        index = 3
        self.assertEqual(find_Element(arr, ranges, rotations, index), 4)

    def test_edge_case_zero_rotations(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 0
        index = 3
        self.assertEqual(find_Element(arr, ranges, rotations, index), 3)

    def test_edge_case_negative_rotations(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = -1
        index = 3
        self.assertEqual(find_Element(arr, ranges, rotations, index), 3)
