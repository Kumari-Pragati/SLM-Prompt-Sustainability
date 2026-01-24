import unittest
from mbpp_540_code import find_Diff

class TestFindDiff(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(find_Diff([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(find_Diff([1], 1), 0)

    def test_all_duplicates_array(self):
        self.assertEqual(find_Diff([1, 1, 1, 1], 4), 0)

    def test_no_duplicates_array(self):
        self.assertEqual(find_Diff([1, 2, 3, 4], 4), 0)

    def test_max_min_diff_array(self):
        self.assertEqual(find_Diff([1, 2, 3, 4, 5], 5), 3)

    def test_max_min_diff_array_with_duplicates(self):
        self.assertEqual(find_Diff([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 10), 3)

    def test_max_min_diff_array_with_duplicates_and_zero(self):
        self.assertEqual(find_Diff([0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 12), 3)
