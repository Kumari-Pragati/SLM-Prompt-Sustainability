import unittest
from mbpp_304_code import find_Element

class TestFind_Element(unittest.TestCase):
    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 2
        index = 2
        self.assertEqual(find_Element(arr, ranges, rotations, index), 3)

    def test_edge_case_left(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 0
        index = 0
        self.assertEqual(find_Element(arr, ranges, rotations, index), 1)

    def test_edge_case_right(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 2
        index = 4
        self.assertEqual(find_Element(arr, ranges, rotations, index), 5)

    def test_edge_case_index_out_of_range(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 2
        index = 6
        with self.assertRaises(IndexError):
            find_Element(arr, ranges, rotations, index)

    def test_edge_case_index_equal_to_left(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 2
        index = 1
        self.assertEqual(find_Element(arr, ranges, rotations, index), 2)

    def test_edge_case_index_equal_to_right(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 2
        index = 4
        self.assertEqual(find_Element(arr, ranges, rotations, index), 5)
