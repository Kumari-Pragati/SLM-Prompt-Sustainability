import unittest
from mbpp_846_code import find_platform

class TestFindPlatform(unittest.TestCase):

    def test_find_platform_empty_list(self):
        self.assertEqual(find_platform([], [], 0), 1)

    def test_find_platform_single_element(self):
        self.assertEqual(find_platform([1], [1], 1), 1)

    def test_find_platform_simple(self):
        self.assertEqual(find_platform([1, 2, 3], [2, 3, 4], 3), 3)

    def test_find_platform_complex(self):
        self.assertEqual(find_platform([1, 2, 3, 4, 5], [2, 4, 5, 6, 7], 5), 4)

    def test_find_platform_reverse_order(self):
        self.assertEqual(find_platform([5, 4, 3, 2, 1], [4, 3, 2, 1, 0], 5), 1)

    def test_find_platform_no_match(self):
        self.assertEqual(find_platform([1, 2, 3], [5, 6, 7], 3), 0)
