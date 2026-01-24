import unittest
from mbpp_304_code import find_Element

class TestFindElement(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(0, 2), (1, 3)]
        rotations = 2
        index = 1
        self.assertEqual(find_Element(arr, ranges, rotations, index), 3)

    def test_edge_case_left_boundary(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(0, 2), (1, 3)]
        rotations = 2
        index = 0
        self.assertEqual(find_Element(arr, ranges, rotations, index), 2)

    def test_edge_case_right_boundary(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(0, 2), (1, 3)]
        rotations = 2
        index = 3
        self.assertEqual(find_Element(arr, ranges, rotations, index), 4)

    def test_edge_case_single_element(self):
        arr = [1]
        ranges = [(0, 0)]
        rotations = 1
        index = 0
        self.assertEqual(find_Element(arr, ranges, rotations, index), 1)

    def test_error_case_negative_index(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(0, 2), (1, 3)]
        rotations = 2
        index = -1
        with self.assertRaises(IndexError):
            find_Element(arr, ranges, rotations, index)

    def test_error_case_index_out_of_range(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(0, 2), (1, 3)]
        rotations = 2
        index = 5
        with self.assertRaises(IndexError):
            find_Element(arr, ranges, rotations, index)
