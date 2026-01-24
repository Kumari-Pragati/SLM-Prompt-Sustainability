import unittest
from mbpp_540_code import find_Diff

class TestFindDiff(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Diff([1, 2, 2, 3, 4, 4, 4, 5, 6, 6], 10), 2)

    def test_single_element(self):
        self.assertEqual(find_Diff([1], 1), 0)

    def test_empty_array(self):
        self.assertEqual(find_Diff([], 0), 0)

    def test_all_same_elements(self):
        self.assertEqual(find_Diff([1, 1, 1, 1, 1], 5), 0)

    def test_negative_numbers(self):
        self.assertEqual(find_Diff([-1, 0, 1, 0, -1], 5), 2)

    def test_large_numbers(self):
        self.assertEqual(find_Diff([100, 200, 200, 300, 400, 400, 400, 500, 600, 600], 10), 2)

    def test_duplicate_elements(self):
        self.assertEqual(find_Diff([1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 6], 11), 2)

    def test_sorted_array(self):
        self.assertEqual(find_Diff([1, 2, 2, 3, 4, 4, 4, 5, 6, 6], 10), 2)

    def test_unsorted_array(self):
        self.assertEqual(find_Diff([4, 2, 2, 1, 5, 6, 6, 3, 4, 4], 10), 2)
