import unittest
from mbpp_304_code import find_Element

class TestFindElement(unittest.TestCase):

    def test_find_element_simple(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [[0, 2], [2, 4], [3, 5]]
        rotations = 2
        index = 3
        self.assertEqual(find_Element(arr, ranges, rotations, index), 5)

    def test_find_element_edge_case(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]
        rotations = 5
        index = 0
        self.assertEqual(find_Element(arr, ranges, rotations, index), 1)

    def test_find_element_empty_array(self):
        arr = []
        ranges = [[0, 0], [1, 1], [2, 2]]
        rotations = 3
        index = 0
        self.assertIsNone(find_Element(arr, ranges, rotations, index))

    def test_find_element_out_of_range(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]
        rotations = 5
        index = 6
        self.assertIsNone(find_Element(arr, ranges, rotations, index))
