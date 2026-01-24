import unittest
from mbpp_304_code import find_Element

class TestFindElement(unittest.TestCase):
    def test_simple(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 2
        index = 2
        self.assertEqual(find_Element(arr, ranges, rotations, index), 3)

    def test_edge(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 0
        index = 2
        self.assertEqual(find_Element(arr, ranges, rotations, index), 3)

    def test_edge2(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 1
        index = 2
        self.assertEqual(find_Element(arr, ranges, rotations, index), 3)

    def test_edge3(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 3
        index = 2
        self.assertEqual(find_Element(arr, ranges, rotations, index), 3)

    def test_edge4(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 4
        index = 2
        self.assertEqual(find_Element(arr, ranges, rotations, index), 3)

    def test_edge5(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 5
        index = 2
        self.assertEqual(find_Element(arr, ranges, rotations, index), 3)

    def test_edge6(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 6
        index = 2
        self.assertEqual(find_Element(arr, ranges, rotations, index), 3)

    def test_edge7(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 7
        index = 2
        self.assertEqual(find_Element(arr, ranges, rotations, index), 3)

    def test_edge8(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 8
        index = 2
        self.assertEqual(find_Element(arr, ranges, rotations, index), 3)

    def test_edge9(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 9
        index = 2
        self.assertEqual(find_Element(arr, ranges, rotations, index), 3)

    def test_edge10(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(1, 3), (2, 4), (3, 5)]
        rotations = 10
        index = 2
        self.assertEqual(find_Element(arr, ranges, rotations, index), 3)
