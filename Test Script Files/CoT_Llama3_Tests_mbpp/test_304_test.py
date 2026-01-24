import unittest
from mbpp_304_code import find_Element

class TestFindElement(unittest.TestCase):
    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 2
        index = 2
        self.assertEqual(find_Element(arr, ranges, rotations, index), 3)

    def test_edge_case(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 0
        index = 2
        self.assertEqual(find_Element(arr, ranges, rotations, index), 3)

    def test_edge_case2(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 1
        index = 2
        self.assertEqual(find_Element(arr, ranges, rotations, index), 3)

    def test_invalid_input(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = -1
        index = 2
        with self.assertRaises(IndexError):
            find_Element(arr, ranges, rotations, index)

    def test_invalid_input2(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 3
        index = 2
        with self.assertRaises(IndexError):
            find_Element(arr, ranges, rotations, index)
