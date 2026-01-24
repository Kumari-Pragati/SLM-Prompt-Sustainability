import unittest
from mbpp_769_code import Diff

class TestDiff(unittest.TestCase):

    def test_diff_same_elements(self):
        self.assertEqual(Diff([1, 2, 3], [1, 2, 3]), [])

    def test_diff_unique_elements(self):
        self.assertEqual(Diff([1, 2, 3], [4, 5, 6]), [[1, 2, 3], [4, 5, 6]])

    def test_diff_common_elements(self):
        self.assertEqual(Diff([1, 2, 3], [3, 4, 5]), [[1, 2], [4, 5]])

    def test_diff_empty_lists(self):
        self.assertEqual(Diff([], []), [])

    def test_diff_one_empty_list(self):
        self.assertEqual(Diff([1, 2, 3], []), [[1, 2, 3]])
