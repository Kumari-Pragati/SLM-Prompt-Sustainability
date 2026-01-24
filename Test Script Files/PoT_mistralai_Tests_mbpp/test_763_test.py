import unittest
from mbpp_763_code import find_Min_Diff

class TestFindMinDiff(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5], 5), 0)
        self.assertEqual(find_Min_Diff([1, 1, 1, 1, 1], 5), 0)
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5, 6], 6), 1)

    def test_edge_case_single_element(self):
        self.assertEqual(find_Min_Diff([1], 1), 0)

    def test_edge_case_empty_list(self):
        self.assertEqual(find_Min_Diff([], 0), 0)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(find_Min_Diff([-1, -2, -3], 3), 1)

    def test_edge_case_duplicates(self):
        self.assertEqual(find_Min_Diff([1, 1, 1], 3), 0)

    def test_edge_case_out_of_bounds(self):
        self.assertEqual(find_Min_Diff([1, 2, 3], 4), 10**20)
