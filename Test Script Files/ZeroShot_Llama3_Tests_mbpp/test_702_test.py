import unittest
from mbpp_702_code import removals

class TestRemovals(unittest.TestCase):

    def test_removals(self):
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 1), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 0), 4)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 2), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 3), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 4), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 5), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 6), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 7), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 8), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 9), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 10), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 11), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 12), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 13), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 14), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 15), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 16), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 17), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 18), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 19), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 20), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 21), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 22), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 23), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 24), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 25), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 26), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 27), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 28), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 29), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 30), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 31), 1)
        self.assertEqual