import unittest
from mbpp_540_code import find_Diff

class TestFindDiff(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Diff([1, 1, 2, 2, 3, 4, 4, 5], 8), 2)
        self.assertEqual(find_Diff([1, 1, 1, 2, 2, 3, 4, 4, 5], 9), 3)
        self.assertEqual(find_Diff([1, 1, 1, 1, 2, 2, 3, 4, 4, 5], 10), 4)

    def test_edge_case_single_element(self):
        self.assertEqual(find_Diff([1], 1), 0)

    def test_edge_case_two_elements(self):
        self.assertEqual(find_Diff([1, 1], 2), 0)

    def test_edge_case_duplicates_only(self):
        self.assertEqual(find_Diff([1, 1, 1], 3), 0)

    def test_edge_case_no_duplicates(self):
        self.assertEqual(find_Diff([1, 2, 3], 3), 0)

    def test_corner_case_empty_list(self):
        self.assertEqual(find_Diff([], 0), 0)
