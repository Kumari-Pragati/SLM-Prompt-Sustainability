import unittest
from mbpp_304_code import find_Element

class TestFindElement(unittest.TestCase):

    def test_find_element_normal(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        ranges = [[0, 2], [3, 5], [6, 7]]
        rotations = 2
        index = 4
        expected_output = 5
        self.assertEqual(find_Element(arr, ranges, rotations, index), expected_output)

    def test_find_element_edge_case_left(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        ranges = [[0, 0], [3, 5], [6, 7]]
        rotations = 2
        index = 0
        expected_output = 1
        self.assertEqual(find_Element(arr, ranges, rotations, index), expected_output)

    def test_find_element_edge_case_right(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        ranges = [[0, 2], [3, 6], [6, 7]]
        rotations = 2
        index = 7
        expected_output = 7
        self.assertEqual(find_Element(arr, ranges, rotations, index), expected_output)

    def test_find_element_invalid_input_index_out_of_range(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        ranges = [[0, 2], [3, 5], [6, 7]]
        rotations = 2
        index = -1
        with self.assertRaises(IndexError):
            find_Element(arr, ranges, rotations, index)

    def test_find_element_invalid_input_arr(self):
        arr = [1, 2, 3]
        ranges = [[0, 2], [3, 5], [6, 7]]
        rotations = 2
        index = 4
        with self.assertRaises(ValueError):
            find_Element(arr, ranges, rotations, index)

    def test_find_element_invalid_input_ranges(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        ranges = [[0, -1], [3, 5], [6, 7]]
        rotations = 2
        index = 4
        with self.assertRaises(ValueError):
            find_Element(arr, ranges, rotations, index)

    def test_find_element_invalid_input_rotations(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        ranges = [[0, 2], [3, 5], [6, 7]]
        rotations = -1
        index = 4
        with self.assertRaises(ValueError):
            find_Element(arr, ranges, rotations, index)
