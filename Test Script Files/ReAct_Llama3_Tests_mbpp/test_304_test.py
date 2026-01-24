import unittest
from mbpp_304_code import find_Element

class TestFindElement(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 2
        index = 2
        self.assertEqual(find_Element(arr, ranges, rotations, index), 3)

    def test_edge_case_left(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 1
        index = 0
        self.assertEqual(find_Element(arr, ranges, rotations, index), 1)

    def test_edge_case_right(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 1
        index = 4
        self.assertEqual(find_Element(arr, ranges, rotations, index), 5)

    def test_edge_case_equal(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 1
        index = 3
        self.assertEqual(find_Element(arr, ranges, rotations, index), 3)

    def test_rotations_zero(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 0
        index = 2
        self.assertEqual(find_Element(arr, ranges, rotations, index), 3)

    def test_rotations_negative(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = -1
        index = 2
        self.assertEqual(find_Element(arr, ranges, rotations, index), 3)

    def test_invalid_index(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 1
        index = 6
        with self.assertRaises(IndexError):
            find_Element(arr, ranges, rotations, index)
