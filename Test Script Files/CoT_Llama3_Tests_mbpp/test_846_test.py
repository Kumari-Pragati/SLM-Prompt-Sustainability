import unittest
from mbpp_846_code import find_platform

class TestFindPlatform(unittest.TestCase):
    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        dep = [2, 3, 4, 5, 6]
        n = len(arr)
        self.assertEqual(find_platform(arr, dep, n), 3)

    def test_edge_case(self):
        arr = [1, 2, 3]
        dep = [2, 3, 4]
        n = len(arr)
        self.assertEqual(find_platform(arr, dep, n), 2)

    def test_edge_case2(self):
        arr = [1, 2, 3, 4, 5, 6]
        dep = [2, 3, 4, 5, 6, 7]
        n = len(arr)
        self.assertEqual(find_platform(arr, dep, n), 5)

    def test_invalid_input(self):
        arr = [1, 2, 3]
        dep = [2, 3]
        n = len(arr)
        with self.assertRaises(IndexError):
            find_platform(arr, dep, n)

    def test_empty_input(self):
        arr = []
        dep = []
        n = len(arr)
        with self.assertRaises(IndexError):
            find_platform(arr, dep, n)
