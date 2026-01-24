import unittest
from mbpp_769_code import Diff

class TestDiff(unittest.TestCase):
    def test_empty_lists(self):
        self.assertEqual(Diff([],[]), [])

    def test_single_list(self):
        self.assertEqual(Diff([1,2,3],[]), [1,2,3])
        self.assertEqual(Diff([], [1,2,3]), [1,2,3])

    def test_common_elements(self):
        self.assertEqual(Diff([1,2,3],[1,2,3]), [])
        self.assertEqual(Diff([1,2,3],[1,2,3,4,5]), [4,5])

    def test_non_common_elements(self):
        self.assertEqual(Diff([1,2,3],[4,5,6]), [1,2,3])
        self.assertEqual(Diff([4,5,6],[1,2,3]), [4,5,6])

    def test_duplicates(self):
        self.assertEqual(Diff([1,1,2,3],[1,2,3]), [1,1,2,3])
        self.assertEqual(Diff([1,2,3],[1,1,2,3]), [1,1,2,3])

    def test_order_matters(self):
        self.assertEqual(Diff([1,2,3],[3,2,1]), [1,2,3])
        self.assertEqual(Diff([3,2,1],[1,2,3]), [1,2,3])
