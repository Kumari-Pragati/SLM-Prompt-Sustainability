import unittest
from mbpp_769_code import Diff

class TestDiff(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(Diff([],[]), [])

    def test_single_element_lists(self):
        self.assertEqual(Diff([1],[1]), [])
        self.assertEqual(Diff([1],[2]), [1,2])
        self.assertEqual(Diff([1],[3]), [1,3])
        self.assertEqual(Diff([1,2],[1,2]), [])
        self.assertEqual(Diff([1,2],[1]), [2])
        self.assertEqual(Diff([1,2],[2]), [1])
        self.assertEqual(Diff([1,2],[3]), [1,2,3])

    def test_multiple_element_lists(self):
        self.assertEqual(Diff([1,2,3],[1,2,3]), [])
        self.assertEqual(Diff([1,2,3],[1,2]), [3])
        self.assertEqual(Diff([1,2,3],[1,3]), [2])
        self.assertEqual(Diff([1,2,3],[2,3]), [1])
        self.assertEqual(Diff([1,2,3],[1,2,3,4]), [4])
        self.assertEqual(Diff([1,2,3,4],[1,2,3,4]), [])
        self.assertEqual(Diff([1,2,3,4],[1,2,3]), [4])
        self.assertEqual(Diff([1,2,3,4],[1,2,3,4,5]), [5])

    def test_duplicates(self):
        self.assertEqual(Diff([1,1,2,2,3,3],[1,1,2,2,3,3]), [])
        self.assertEqual(Diff([1,1,2,2,3,3],[1,1,2,2]), [3,3])
        self.assertEqual(Diff([1,1,2,2,3,3],[1,1,2,3]), [2,2])
        self.assertEqual(Diff([1,1,2,2,3,3],[1,1,2,3,4]), [3,3,4])
