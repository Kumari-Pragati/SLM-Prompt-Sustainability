import unittest
from mbpp_763_code import find_Min_Diff

class TestFindMinDiff(unittest.TestCase):

    def test_empty_list(self):
        self.assertAlmostEqual(find_Min_Diff([], 0), 0)

    def test_single_element(self):
        self.assertAlmostEqual(find_Min_Diff([1], 1), 0)

    def test_sorted_ascending(self):
        self.assertAlmostEqual(find_Min_Diff([1, 2, 3, 4, 5], 5), 1)

    def test_sorted_descending(self):
        self.assertAlmostEqual(find_Min_Diff([5, 4, 3, 2, 1], 5), 1)

    def test_duplicates(self):
        self.assertAlmostEqual(find_Min_Diff([1, 1, 2, 2, 3], 5), 0)

    def test_negative_numbers(self):
        self.assertAlmostEqual(find_Min_Diff([-1, -2, -3], 3), 1)

    def test_large_numbers(self):
        self.assertAlmostEqual(find_Min_Diff([1000000001, 1000000002, 1000000003], 3), 1)

    def test_out_of_bounds(self):
        self.assertRaises(IndexError, find_Min_Diff, [1, 2, 3], 4)

    def test_negative_n(self):
        self.assertRaises(ValueError, find_Min_Diff, [1, 2, 3], -1)
