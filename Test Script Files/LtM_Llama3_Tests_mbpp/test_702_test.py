import unittest
from mbpp_702_code import removals

class TestRemovals(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 0), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 1), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 2), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 3), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 4), 1)

    def test_edge(self):
        self.assertEqual(removals([], 0, 0), 0)
        self.assertEqual(removals([1], 1, 0), 0)
        self.assertEqual(removals([1, 2], 2, 0), 1)
        self.assertEqual(removals([1, 2, 3], 3, 0), 2)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 5), 0)

    def test_complex(self):
        self.assertEqual(removals([1, 2, 3, 4, 5, 6], 6, 1), 2)
        self.assertEqual(removals([1, 2, 3, 4, 5, 6, 7], 7, 2), 3)
        self.assertEqual(removals([1, 2, 3, 4, 5, 6, 7, 8], 8, 3), 4)
        self.assertEqual(removals([1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 4), 5)
