import unittest
from mbpp_831_code import count_Pairs

class TestCountPairs(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(count_Pairs([1, 2, 2, 3, 3, 4], 6), 2)

    def test_edge_case_start(self):
        self.assertEqual(count_Pairs([1, 1], 2), 1)

    def test_edge_case_end(self):
        self.assertEqual(count_Pairs([1, 2, 2], 3), 1)

    def test_edge_case_empty(self):
        self.assertEqual(count_Pairs([], 0), 0)

    def test_edge_case_single(self):
        self.assertEqual(count_Pairs([1], 1), 0)

    def test_edge_case_duplicate(self):
        self.assertEqual(count_Pairs([1, 1], 1), 0)

    def test_negative_input(self):
        self.assertRaises(ValueError, count_Pairs, [-1, -2], -1)

    def test_negative_array_len(self):
        self.assertRaises(ValueError, count_Pairs, [1, 2, 3], -1)
