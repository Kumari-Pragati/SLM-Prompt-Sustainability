import unittest
from mbpp_540_code import find_Diff

class TestFindDiff(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_Diff([], 0), 0)

    def test_single_element(self):
        self.assertEqual(find_Diff([1], 1), 0)

    def test_single_duplicate(self):
        self.assertEqual(find_Diff([1, 1], 2), 0)

    def test_multiple_duplicates(self):
        self.assertEqual(find_Diff([1, 1, 2, 2, 3, 3, 4, 4, 4], 9), 0)

    def test_no_duplicates(self):
        self.assertEqual(find_Diff([1, 2, 3, 4, 5], 5), 0)

    def test_reverse_order(self):
        self.assertEqual(find_Diff([4, 3, 2, 1], 4), 0)

    def test_negative_numbers(self):
        self.assertEqual(find_Diff([-1, -2, -3, -4], 4), 0)

    def test_mixed_positive_and_negative(self):
        self.assertEqual(find_Diff([1, -2, 3, -4, 5], 5), 0)

    def test_single_negative_and_positive(self):
        self.assertEqual(find_Diff([-1, 1], 2), 1)

    def test_single_element_list_length_greater_than_n(self):
        self.assertEqual(find_Diff([1], 2), 0)

    def test_n_greater_than_list_length(self):
        self.assertEqual(find_Diff([1, 2, 3], 4), 0)

    def test_list_with_only_max_value(self):
        self.assertEqual(find_Diff([999999999], 1), 0)

    def test_list_with_only_min_value(self):
        self.assertEqual(find_Diff([-999999999], 1), 0)
