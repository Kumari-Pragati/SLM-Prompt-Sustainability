import unittest
from mbpp_564_code import count_Pairs

class TestCountPairs(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(count_Pairs([1, 2, 3, 4, 5], 5), 10)
        self.assertEqual(count_Pairs([2, 2, 2, 2, 2], 5), 4)

    def test_edge_case_empty_list(self):
        self.assertEqual(count_Pairs([], 0), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(count_Pairs([1], 1), 0)

    def test_edge_case_single_pair(self):
        self.assertEqual(count_Pairs([1, 1], 2), 1)

    def test_edge_case_duplicate_elements(self):
        self.assertEqual(count_Pairs([1, 1, 1, 1], 4), 3)

    def test_edge_case_out_of_range(self):
        self.assertRaises(IndexError, lambda: count_Pairs([1, 2, 3], -1))
