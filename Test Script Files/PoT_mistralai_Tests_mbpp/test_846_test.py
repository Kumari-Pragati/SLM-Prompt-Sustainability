import unittest
from mbpp_846_code import find_platform

class TestFindPlatform(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_platform([1, 2, 3, 4], [2, 3, 4, 6], 4), 4)
        self.assertEqual(find_platform([1, 2, 3, 4], [2, 3, 4, 5], 4), 4)
        self.assertEqual(find_platform([1, 2, 3, 4], [1, 2, 3, 4], 4), 1)

    def test_edge_case_1(self):
        self.assertEqual(find_platform([1, 2, 3], [2, 3, 4], 3), 3)
        self.assertEqual(find_platform([1, 2, 3], [2, 3, 4], 2), 1)
        self.assertEqual(find_platform([1, 2, 3], [2, 3, 4], 1), 1)

    def test_edge_case_2(self):
        self.assertEqual(find_platform([1, 2, 3], [1, 2, 5], 3), 2)
        self.assertEqual(find_platform([1, 2, 3], [1, 5, 5], 2), 1)
        self.assertEqual(find_platform([1, 2, 3], [1, 5, 5], 1), 1)

    def test_corner_case(self):
        self.assertEqual(find_platform([], [], 0), 0)
        self.assertEqual(find_platform([1], [], 0), 0)
        self.assertEqual(find_platform([], [1], 0), 0)
        self.assertEqual(find_platform([1], [1], 0), 1)
