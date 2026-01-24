import unittest
from mbpp_304_code import find_Element

class TestFindElement(unittest.TestCase):
    def test_typical_input(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 2
        index = 3
        self.assertEqual(find_Element(arr, ranges, rotations, index), 5)

    def test_edge_case_index_at_left_range(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 2
        index = 1
        self.assertEqual(find_Element(arr, ranges, rotations, index), 1)

    def test_edge_case_index_at_right_range(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 2
        index = 4
        self.assertEqual(find_Element(arr, ranges, rotations, index), 5)

    def test_edge_case_index_at_middle_range(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 2
        index = 3
        self.assertEqual(find_Element(arr, ranges, rotations, index), 5)

    def test_edge_case_index_at_left_range_rotations(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 3
        index = 1
        self.assertEqual(find_Element(arr, ranges, rotations, index), 1)

    def test_edge_case_index_at_right_range_rotations(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 3
        index = 4
        self.assertEqual(find_Element(arr, ranges, rotations, index), 5)

    def test_edge_case_index_at_middle_range_rotations(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 3
        index = 3
        self.assertEqual(find_Element(arr, ranges, rotations, index), 5)

    def test_invalid_input_type(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 2
        index = 'a'
        with self.assertRaises(TypeError):
            find_Element(arr, ranges, rotations, index)

    def test_invalid_input_range_type(self):
        arr = [1, 2, 3, 4, 5]
        ranges = 'abc'
        rotations = 2
        index = 3
        with self.assertRaises(TypeError):
            find_Element(arr, ranges, rotations, index)

    def test_invalid_input_arr_type(self):
        arr = 'abc'
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 2
        index = 3
        with self.assertRaises(TypeError):
            find_Element(arr, ranges, rotations, index)
