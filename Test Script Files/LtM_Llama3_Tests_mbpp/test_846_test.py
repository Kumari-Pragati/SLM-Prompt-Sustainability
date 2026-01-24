import unittest
from mbpp_846_code import find_platform

class TestFindPlatform(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(find_platform([1, 2, 3], [2, 3, 4], 3), 2)
        self.assertEqual(find_platform([1, 2, 3], [1, 2, 3], 3), 3)
        self.assertEqual(find_platform([1, 2, 3], [3, 4, 5], 3), 1)

    def test_edge(self):
        self.assertEqual(find_platform([], [], 0), 0)
        self.assertEqual(find_platform([1], [1], 1), 1)
        self.assertEqual(find_platform([1, 2, 3], [], 3), 1)
        self.assertEqual(find_platform([], [1, 2, 3], 3), 1)

    def test_complex(self):
        self.assertEqual(find_platform([1, 2, 3, 4, 5], [2, 3, 4, 5, 6], 5), 3)
        self.assertEqual(find_platform([1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7], 6), 4)
        self.assertEqual(find_platform([1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 4, 5, 6, 7, 8, 9, 10], 9), 7)
