import unittest
from mbpp_304_code import find_Element

class TestFindElement(unittest.TestCase):

    def test_find_Element(self):
        arr = [1, 2, 3, 4, 5]
        ranges = [(0, 2), (1, 3)]
        rotations = 2
        index = 2
        self.assertEqual(find_Element(arr, ranges, rotations, index), 3)

        arr = [10, 20, 30, 40, 50]
        ranges = [(0, 4)]
        rotations = 1
        index = 2
        self.assertEqual(find_Element(arr, ranges, rotations, index), 30)

        arr = [100, 200, 300, 400, 500]
        ranges = [(0, 1), (2, 3), (4, 4)]
        rotations = 3
        index = 3
        self.assertEqual(find_Element(arr, ranges, rotations, index), 400)

        arr = [1000, 2000, 3000, 4000, 5000]
        ranges = [(0, 0), (1, 2), (3, 4)]
        rotations = 3
        index = 0
        self.assertEqual(find_Element(arr, ranges, rotations, index), 1000)
