import unittest
from mbpp_304_code import find_Element

class TestFindElement(unittest.TestCase):

    def test_simple_input(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [[0, 2], [1, 3]]
        rotations = 2
        index = 1
        self.assertEqual(find_Element(arr, ranges, rotations, index), 2)

    def test_edge_conditions(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [[0, 2], [1, 3]]
        rotations = 2
        index = 0
        self.assertEqual(find_Element(arr, ranges, rotations, index), 1)

        arr = [1, 2, 3, 4, 5]
        ranges = [[0, 2], [1, 3]]
        rotations = 2
        index = 4
        self.assertEqual(find_Element(arr, ranges, rotations, index), 5)

    def test_complex_cases(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [[0, 2], [1, 3]]
        rotations = 2
        index = 3
        self.assertEqual(find_Element(arr, ranges, rotations, index), 4)

        arr = [1, 2, 3, 4, 5]
        ranges = [[0, 2], [1, 3]]
        rotations = 2
        index = 2
        self.assertEqual(find_Element(arr, ranges, rotations, index), 3)

        arr = [1, 2, 3, 4, 5]
        ranges = [[0, 2], [1, 3]]
        rotations = 2
        index = 1
        self.assertEqual(find_Element(arr, ranges, rotations, index), 2)

        arr = [1, 2, 3, 4, 5]
        ranges = [[0, 2], [1, 3]]
        rotations = 2
        index = 0
        self.assertEqual(find_Element(arr, ranges, rotations, index), 1)
