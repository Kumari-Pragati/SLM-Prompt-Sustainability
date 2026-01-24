import unittest
from mbpp_304_code import find_Element

class TestFindElement(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [[0, 2], [1, 3]]
        rotations = 2
        index = 1
        self.assertEqual(find_Element(arr, ranges, rotations, index), 2)

    def test_edge_case_left_boundary(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [[0, 2], [1, 3]]
        rotations = 2
        index = 0
        self.assertEqual(find_Element(arr, ranges, rotations, index), 1)

    def test_edge_case_right_boundary(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [[0, 2], [1, 3]]
        rotations = 2
        index = 4
        self.assertEqual(find_Element(arr, ranges, rotations, index), 5)

    def test_special_case_rotation(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [[0, 2], [1, 3]]
        rotations = 1
        index = 1
        self.assertEqual(find_Element(arr, ranges, rotations, index), 2)

    def test_invalid_input_rotations(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [[0, 2], [1, 3]]
        rotations = -1
        index = 1
        with self.assertRaises(Exception):
            find_Element(arr, ranges, rotations, index)

    def test_invalid_input_index(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [[0, 2], [1, 3]]
        rotations = 2
        index = 5
        with self.assertRaises(Exception):
            find_Element(arr, ranges, rotations, index)
