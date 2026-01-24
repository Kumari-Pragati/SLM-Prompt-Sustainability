import unittest
from mbpp_842_code import get_odd_occurence

class TestGetOddOccurence(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(get_odd_occurence([1, 2, 3, 2, 2, 4, 4, 1], 8), 1)
        self.assertEqual(get_odd_occurence([4, 4, 4, 4, 4, 4, 4, 4], 8), -1)
        self.assertEqual(get_odd_occurence([1, 1, 1, 2, 2, 3, 3, 3], 8), 2)

    def test_edge_case_single_element(self):
        self.assertEqual(get_odd_occurence([1], 1), 1)

    def test_edge_case_empty_list(self):
        self.assertEqual(get_odd_occurence([], 0), -1)

    def test_edge_case_all_same(self):
        self.assertEqual(get_odd_occurence([1], 1), 1)
        self.assertEqual(get_odd_occurence([0], 1), -1)

    def test_corner_case_all_even(self):
        self.assertEqual(get_odd_occurence([2, 2, 2, 2], 4), -1)
