import unittest
from mbpp_763_code import find_Min_Diff

class TestFindMinDiff(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Min_Diff([1, 5, 3, 19, 18, 25], 6), 1)

    def test_edge_case_single_element(self):
        self.assertEqual(find_Min_Diff([5], 1), 0)

    def test_boundary_case_empty_array(self):
        self.assertEqual(find_Min_Diff([], 0), None)

    def test_corner_case_repeated_elements(self):
        self.assertEqual(find_Min_Diff([1, 1, 1, 1], 4), 0)

    def test_corner_case_sorted_array(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4], 4), 1)

    def test_corner_case_reverse_sorted_array(self):
        self.assertEqual(find_Min_Diff([4, 3, 2, 1], 4), 1)

    def test_corner_case_large_numbers(self):
        self.assertEqual(find_Min_Diff([10**6, 2*10**6, 3*10**6], 3), 10**6)
