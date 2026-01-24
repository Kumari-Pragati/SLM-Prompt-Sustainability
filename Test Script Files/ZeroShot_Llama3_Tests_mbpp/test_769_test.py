import unittest
from mbpp_769_code import Diff

class TestDiff(unittest.TestCase):

    def test_diff(self):
        self.assertEqual(Diff([1,2,3,4,5], [5,6,7,8,9]), [[1,2,3,4], [6,7,8,9]])
        self.assertEqual(Diff([1,2,3,4,5], [1,2,3,4,5]), [])
        self.assertEqual(Diff([1,2,3,4,5], [1,2,3]), [[4,5]])
        self.assertEqual(Diff([1,2,3,4,5], [5,6,7,8,9,10]), [[1,2,3,4], [6,7,8,9,10]])
        self.assertEqual(Diff([1,2,3,4,5], [1,2,3,4,5,6,7,8,9,10]), [])

    def test_diff_empty(self):
        self.assertEqual(Diff([], []), [])
        self.assertEqual(Diff([1,2,3], []), [[1,2,3]])
        self.assertEqual(Diff([], [1,2,3]), [[1,2,3]])
        self.assertEqual(Diff([], [1,2,3,4,5]), [])
        self.assertEqual(Diff([1,2,3,4,5], []), [[1,2,3,4,5]])
