import unittest
from mbpp_846_code import find_platform

class TestFindPlatform(unittest.TestCase):

    def test_find_platform(self):
        self.assertEqual(find_platform([1, 3, 5, 7, 9], [2, 4, 8, 12], 5), 3)
        self.assertEqual(find_platform([1, 2, 3, 4, 5], [2, 3, 4, 5, 6], 5), 2)
        self.assertEqual(find_platform([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 5), 1)
        self.assertEqual(find_platform([1, 2, 3, 4, 5], [5, 6, 7, 8, 9], 5), 1)
        self.assertEqual(find_platform([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6], 6), 2)
