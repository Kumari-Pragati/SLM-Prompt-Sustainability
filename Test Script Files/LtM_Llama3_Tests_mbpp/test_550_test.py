import unittest
from mbpp_550_code import find_Max

class TestFindMax(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(find_Max([1, 2, 3, 4, 5], 0, 4), 5)
        self.assertEqual(find_Max([5, 4, 3, 2, 1], 0, 4), 5)
        self.assertEqual(find_Max([1, 1, 1, 1, 1], 0, 4), 1)

    def test_edge(self):
        self.assertEqual(find_Max([1], 0, 0), 1)
        self.assertEqual(find_Max([1, 2], 0, 1), 2)
        self.assertEqual(find_Max([1, 2, 3], 0, 2), 3)

    def test_empty(self):
        with self.assertRaises(IndexError):
            find_Max([], 0, 0)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            find_Max("hello", 0, 0)
