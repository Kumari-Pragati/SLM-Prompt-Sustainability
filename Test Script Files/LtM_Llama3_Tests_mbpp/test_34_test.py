import unittest
from mbpp_34_code import find_missing

class TestFindMissing(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(find_missing([1, 2, 3, 4, 5], 5), 6)
        self.assertEqual(find_missing([1, 2, 3, 5, 6], 6), 4)
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 11)

    def test_edge(self):
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 10)
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6, 7, 8], 8), 9)
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6, 7], 7), 8)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            find_missing([], 5)
        with self.assertRaises(TypeError):
            find_missing([1, 2, 3, 4, 5], 'a')
        with self.assertRaises(TypeError):
            find_missing([1, 2, 3, 4, 5], -1)
