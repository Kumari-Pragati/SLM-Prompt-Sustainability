import unittest
from mbpp_702_code import removals

class TestRemovals(unittest.TestCase):

    def test_removals(self):
        self.assertEqual(removals([1, 3, 4, 9, 10, 11, 12, 17, 20], 9, 4), 5)
        self.assertEqual(removals([10, 10, 10, 10, 10, 10, 10, 10, 10, 10], 10, 0), 10)
        self.assertEqual(removals([1, 5, 6, 8, 9, 15, 18, 20, 21, 22], 10, 3), 4)
        self.assertEqual(removals([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 1), 1)
        self.assertEqual(removals([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 10, 1), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 10), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 0), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 5), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 6), 0)
