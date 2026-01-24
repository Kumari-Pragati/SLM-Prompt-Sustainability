import unittest
from mbpp_769_code import Diff

class TestDiff(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(Diff([1,2,3,4,5],[2,4,6]), [1,3,5,2,4,6])

    def test_empty(self):
        self.assertEqual(Diff([],[]), [])
        self.assertEqual(Diff([1,2,3],[]), [1,2,3])
        self.assertEqual(Diff([], [1,2,3]), [1,2,3])

    def test_single(self):
        self.assertEqual(Diff([1,2,3],[]), [1,2,3])
        self.assertEqual(Diff([], [1,2,3]), [1,2,3])

    def test_duplicates(self):
        self.assertEqual(Diff([1,2,2,3,4,4,5],[2,2,4,4,6]), [1,3,5,2,4,6])

    def test_duplicates_same(self):
        self.assertEqual(Diff([1,2,2,3,4,4,5],[1,2,2,3,4,4,5]), [])

    def test_duplicates_diff(self):
        self.assertEqual(Diff([1,2,3,4,5],[1,2,3,4,5]), [])
