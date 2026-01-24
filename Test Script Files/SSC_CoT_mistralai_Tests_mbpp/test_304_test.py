import unittest
from mbpp_304_code import find_Element

class TestFindElement(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 2), (2, 4)], 1, 2), 3)
        self.assertEqual(find_Element([6, 7, 8, 9, 10], [(3, 5), (1, 3)], 2, 7), 8)

    def test_edge_input(self):
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 2), (2, 4)], 1, 0), 1)
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [(0, 2), (2, 4)], 1, 5), 5)
        self.assertEqual(find_Element([6, 7, 8, 9, 10], [(3, 5), (1, 3)], 2, 0), 6)
        self.assertEqual(find_Element([6, 7, 8, 9, 10], [(3, 5), (1, 3)], 2, 6), 10)

    def test_empty_input(self):
        with self.assertRaises(IndexError):
            find_Element([], [], 0, 0)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            find_Element([1, 2, 3], [(0, 2), (2, 4)], 0, -1)
        with self.assertRaises(ValueError):
            find_Element([1, 2, 3], [(0, 2), (2, 4)], 0, len([1, 2, 3]) + 1)
        with self.assertRaises(ValueError):
            find_Element([1, 2, 3], [], 0, 0)
        with self.assertRaises(ValueError):
            find_Element([1, 2, 3], [(0, 2), (2, 4)], 0, -1)
        with self.assertRaises(ValueError):
            find_Element([1, 2, 3], [(0, 2), (2, 4)], len([1, 2, 3]) + 1, 0)
