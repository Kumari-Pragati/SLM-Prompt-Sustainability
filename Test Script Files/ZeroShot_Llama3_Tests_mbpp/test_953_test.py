import unittest
from mbpp_953_code import subset

class TestSubset(unittest.TestCase):

    def test_subset(self):
        self.assertEqual(subset([1, 2, 2, 3, 3, 3], 6), 3)
        self.assertEqual(subset([1, 2, 3, 4, 5], 5), 1)
        self.assertEqual(subset([1, 1, 1, 1, 1], 5), 5)
        self.assertEqual(subset([], 0), 0)
        self.assertEqual(subset([1], 1), 1)
        self.assertEqual(subset([1, 2], 2, ), 1)
        self.assertEqual(subset([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10], 20), 1)
        self.assertEqual(subset([1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10], 30), 1)
        self.assertEqual(subset([1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10], 30), 1)
