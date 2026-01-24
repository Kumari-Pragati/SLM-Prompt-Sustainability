import unittest
from mbpp_304_code import find_Element

class TestFindElement(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [[0, 2], [1, 3]]
        rotations = 2
        index = 1
        self.assertEqual(find_Element(arr, ranges, rotations, index), 2)

    def test_edge_boundary_condition(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [[0, 2], [1, 3]]
        rotations = 2
        index = 0
        self.assertEqual(find_Element(arr, ranges, rotations, index), 1)

    def test_invalid_input(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [[0, 2], [1, 3]]
        rotations = 2
        index = 5
        with self.assertRaises(IndexError):
            find_Element(arr, ranges, rotations, index)
