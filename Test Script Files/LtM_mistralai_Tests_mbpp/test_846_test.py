import unittest
from mbpp_846_code import find_platform

class TestFindPlatform(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(find_platform([1, 2, 3], [2, 3, 4], 3), 1)
        self.assertEqual(find_platform([1, 2, 3], [1, 2, 3], 3), 1)
        self.assertEqual(find_platform([1, 2, 3], [4, 5, 6], 3), 0)

    def test_edge_cases(self):
        self.assertEqual(find_platform([], [], 0), 0)
        self.assertEqual(find_platform([1], [1], 1), 1)
        self.assertEqual(find_platform([1, 2], [2, 1], 2), 1)
        self.assertEqual(find_platform([1, 2, 3], [1, 2, 3, 4], 4), 3)
        self.assertEqual(find_platform([1, 2, 3], [1, 2, 4], 3), 2)

    def test_complex(self):
        self.assertEqual(find_platform([1, 2, 3, 4], [2, 3, 4, 5], 4), 3)
        self.assertEqual(find_platform([1, 2, 3, 4], [1, 2, 5, 6], 4), 2)
        self.assertEqual(find_platform([1, 2, 3, 4], [1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(find_platform([1, 2, 3, 4], [1, 2, 3, 5, 6], 5), 3)
