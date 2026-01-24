import unittest
from mbpp_540_code import find_Diff

class TestFindDiff(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(find_Diff([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(find_Diff([1], 1), 0)

    def test_all_duplicates_array(self):
        self.assertEqual(find_Diff([1, 1, 1, 1, 1], 5), 0)

    def test_all_unique_array(self):
        self.assertEqual(find_Diff([1, 2, 3, 4, 5], 5), 5)

    def test_max_min_diff(self):
        self.assertEqual(find_Diff([1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9], 11), 4)

    def test_max_min_diff_with_zero(self):
        self.assertEqual(find_Diff([1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 0], 12), 4)

    def test_max_min_diff_with_negative(self):
        self.assertEqual(find_Diff([-1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -9], 11), 4)
