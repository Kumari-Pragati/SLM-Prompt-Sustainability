import unittest
from mbpp_702_code import removals

class TestRemovals(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(removals([], 0, 0), 0)

    def test_single_element(self):
        self.assertEqual(removals([1], 1, 0), 0)
        self.assertEqual(removals([1], 1, 1), 0)

    def test_small_list(self):
        self.assertEqual(removals([1, 2, 3, 4], 4, 1), 2)
        self.assertEqual(removals([1, 2, 3, 4], 4, 2), 1)
        self.assertEqual(removals([1, 2, 3, 4], 4, 3), 0)

    def test_large_list(self):
        arr = [1] * 1000 + [2] * 1000 + [3] * 1000
        self.assertEqual(removals(arr, 3000, 1), 2000)
        self.assertEqual(removals(arr, 3000, 2), 1000)
        self.assertEqual(removals(arr, 3000, 3), 0)
