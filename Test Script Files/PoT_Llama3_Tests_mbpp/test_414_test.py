import unittest
from mbpp_414_code import overlapping

class TestOverlapping(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(overlapping([1, 2, 3], [4, 5, 6]), 0)

    def test_edge_case_empty_list1(self):
        self.assertEqual(overlapping([], [1, 2, 3]), 0)

    def test_edge_case_empty_list2(self):
        self.assertEqual(overlapping([1, 2, 3], []), 0)

    def test_edge_case_single_element_list1(self):
        self.assertEqual(overlapping([1], [1, 2, 3]), 1)

    def test_edge_case_single_element_list2(self):
        self.assertEqual(overlapping([1, 2, 3], [1]), 1)

    def test_edge_case_equal_lists(self):
        self.assertEqual(overlapping([1, 2, 3], [1, 2, 3]), 1)

    def test_edge_case_reverse_lists(self):
        self.assertEqual(overlapping([1, 2, 3], [3, 2, 1]), 1)

    def test_edge_case_lists_of_different_lengths(self):
        self.assertEqual(overlapping([1, 2, 3], [1, 2]), 0)

    def test_edge_case_lists_of_same_length(self):
        self.assertEqual(overlapping([1, 2, 3], [1, 2, 3]), 1)

    def test_edge_case_lists_of_zero_length(self):
        self.assertEqual(overlapping([], []), 0)
