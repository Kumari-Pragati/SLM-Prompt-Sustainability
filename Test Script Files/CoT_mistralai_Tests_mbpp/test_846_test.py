import unittest
from mbpp_846_code import find_platform

class TestFindPlatform(unittest.TestCase):
    def test_find_platform_typical_case(self):
        self.assertEqual(find_platform([1, 2, 3], [2, 3, 4], 3), 3)
        self.assertEqual(find_platform([1, 2, 3], [2, 3, 4, 5], 4), 4)
        self.assertEqual(find_platform([1, 2, 3, 4], [2, 3, 4, 5], 4), 4)

    def test_find_platform_edge_case(self):
        self.assertEqual(find_platform([1], [2], 1), 1)
        self.assertEqual(find_platform([1, 2], [], 0), 0)
        self.assertEqual(find_platform([1, 2], [1], 1), 1)
        self.assertEqual(find_platform([1, 2], [2, 1], 2), 2)
        self.assertEqual(find_platform([1, 2, 3], [1, 2, 3], 3), 3)
        self.assertEqual(find_platform([1, 2, 3], [1, 2, 4], 3), 3)
        self.assertEqual(find_platform([1, 2, 3], [1, 2, 4, 5], 4), 4)

    def test_find_platform_invalid_inputs(self):
        self.assertRaises(ValueError, find_platform, [], [], 0)
        self.assertRaises(ValueError, find_platform, [1], [2], -1)
        self.assertRaises(ValueError, find_platform, [1], [], -1)
