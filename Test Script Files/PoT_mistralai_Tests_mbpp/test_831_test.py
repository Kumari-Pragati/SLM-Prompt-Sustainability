import unittest
from mbpp_831_code import count_Pairs

class TestCountPairs(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_Pairs([1, 2, 2, 3, 3, 4, 4], 7), 3)

    def test_edge_case_empty_list(self):
        self.assertEqual(count_Pairs([], 0), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(count_Pairs([1], 1), 0)

    def test_edge_case_duplicates_at_boundary(self):
        self.assertEqual(count_Pairs([1, 1], 2), 1)

    def test_corner_case_all_duplicates(self):
        self.assertEqual(count_Pairs([1, 1, 1], 3), 2)
