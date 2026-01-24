import unittest
from mbpp_304_code import find_Element

class TestFindElement(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [[0, 2], [1, 3]]
        rotations = 2
        index = 1
        self.assertEqual(find_Element(arr, ranges, rotations, index), 2)

    def test_edge_case_with_single_rotation(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [[0, 2]]
        rotations = 1
        index = 1
        self.assertEqual(find_Element(arr, ranges, rotations, index), 3)

    def test_boundary_case_with_multiple_rotations(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [[0, 2], [1, 3], [2, 4]]
        rotations = 3
        index = 0
        self.assertEqual(find_Element(arr, ranges, rotations, index), 1)

    def test_corner_case_with_no_rotation(self):
        arr = [1, 2, 3, 4, 5]
        ranges = []
        rotations = 0
        index = 2
        self.assertEqual(find_Element(arr, ranges, rotations, index), 3)

    def test_invalid_index(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [[0, 2], [1, 3]]
        rotations = 2
        index = 5
        with self.assertRaises(IndexError):
            find_Element(arr, ranges, rotations, index)
