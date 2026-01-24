import unittest
from mbpp_564_code import count_Pairs

class TestCountPairs(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_Pairs([1, 2, 3, 4, 5], 5), 10)
        self.assertEqual(count_Pairs([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 10), 20)
        self.assertEqual(count_Pairs([0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 12), 22)

    def test_edge_case_empty(self):
        self.assertEqual(count_Pairs([], 0), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(count_Pairs([1], 1), 0)

    def test_edge_case_two_elements(self):
        self.assertEqual(count_Pairs([1, 1], 2), 1)

    def test_corner_case_duplicates_at_start(self):
        self.assertEqual(count_Pairs([1, 1, 2, 2, 3], 5), 6)

    def test_corner_case_duplicates_at_end(self):
        self.assertEqual(count_Pairs([1, 2, 2, 3, 3], 5), 4)
