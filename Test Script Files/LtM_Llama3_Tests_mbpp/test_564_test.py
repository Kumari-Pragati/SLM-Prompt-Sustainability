import unittest
from mbpp_564_code import count_Pairs

class TestCountPairs(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(count_Pairs([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(count_Pairs([1], 1), 0)

    def test_two_element_array(self):
        self.assertEqual(count_Pairs([1, 2], 2), 1)

    def test_three_element_array(self):
        self.assertEqual(count_Pairs([1, 2, 3], 3), 2)

    def test_duplicates(self):
        self.assertEqual(count_Pairs([1, 2, 2, 3], 4), 2)

    def test_all_duplicates(self):
        self.assertEqual(count_Pairs([1, 1, 1, 1], 4, 1), 0)

    def test_all_duplicates_edge_case(self):
        self.assertEqual(count_Pairs([1, 1, 1, 1, 1], 5, 1), 0)

    def test_all_duplicates_edge_case2(self):
        self.assertEqual(count_Pairs([1, 1, 1, 1, 1, 1], 6, 1), 0)

    def test_all_duplicates_edge_case3(self):
        self.assertEqual(count_Pairs([1, 1, 1, 1, 1, 1, 1], 7, 1), 0)

    def test_all_duplicates_edge_case4(self):
        self.assertEqual(count_Pairs([1, 1, 1, 1, 1, 1, 1, 1], 8, 1), 0)

    def test_all_duplicates_edge_case5(self):
        self.assertEqual(count_Pairs([1, 1, 1, 1, 1, 1, 1, 1, 1], 9, 1), 0)
