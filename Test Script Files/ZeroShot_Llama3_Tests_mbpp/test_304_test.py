import unittest
from mbpp_304_code import find_Element

class TestFindElement(unittest.TestCase):

    def test_find_element(self):
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [[1, 5], [2, 4]], 2, 2), 3)
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [[1, 5], [2, 4]], 1, 2), 2)
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [[1, 5], [2, 4]], 0, 2), 2)
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [[1, 5], [2, 4]], 3, 2), 3)
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [[1, 5], [2, 4]], 2, 0), 1)
        self.assertEqual(find_Element([1, 2, 3, 4, 5], [[1, 5], [2, 4]], 1, 0), 1)

    def test_find_element_invalid_index(self):
        with self.assertRaises(IndexError):
            find_Element([1, 2, 3, 4, 5], [[1, 5], [2, 4]], 2, 6)

    def test_find_element_invalid_rotations(self):
        with self.assertRaises(IndexError):
            find_Element([1, 2, 3, 4, 5], [[1, 5], [2, 4]], 0, 2)
