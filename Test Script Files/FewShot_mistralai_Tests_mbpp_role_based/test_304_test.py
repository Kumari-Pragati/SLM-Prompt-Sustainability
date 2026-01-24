import unittest
from mbpp_304_code import find_Element

class TestFindElement(unittest.TestCase):
    def test_valid_input(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [[0, 2], [2, 4], [4, 5]]
        rotations = 3
        index = 3
        self.assertEqual(find_Element(arr, ranges, rotations, index), 5)

    def test_empty_array(self):
        arr = []
        with self.assertRaises(IndexError):
            find_Element(arr, [], 0, 0)

    def test_out_of_range_index(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [[0, 2], [2, 4], [4, 5]]
        rotations = 3
        index = -1
        with self.assertRaises(IndexError):
            find_Element(arr, ranges, rotations, index)

    def test_invalid_rotation(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [[0, 2], [2, 4], [4, 5]]
        rotations = -1
        index = 3
        with self.assertRaises(ValueError):
            find_Element(arr, ranges, rotations, index)

    def test_invalid_range(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [[0, -1], [2, 4], [4, 5]]
        rotations = 3
        index = 3
        with self.assertRaises(ValueError):
            find_Element(arr, ranges, rotations, index)
