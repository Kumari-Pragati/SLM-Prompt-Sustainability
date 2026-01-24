import unittest
from mbpp_564_code import count_Pairs

class TestCountPairs(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Pairs([1, 2, 3, 4, 5], 5), 4)

    def test_edge_case(self):
        self.assertEqual(count_Pairs([1, 1, 1, 1, 1], 5), 0)

    def test_edge_case2(self):
        self.assertEqual(count_Pairs([1, 2, 3, 4, 5, 5], 6), 4)

    def test_edge_case3(self):
        self.assertEqual(count_Pairs([1, 1, 2, 2, 3, 3], 6), 3)

    def test_edge_case4(self):
        self.assertEqual(count_Pairs([1, 2, 3, 4, 5, 6], 6), 5)

    def test_edge_case5(self):
        self.assertEqual(count_Pairs([1, 2, 3, 4, 5, 6, 7], 7), 6)

    def test_edge_case6(self):
        self.assertEqual(count_Pairs([1, 1, 1, 1, 1, 1, 1], 7), 0)

    def test_edge_case7(self):
        self.assertEqual(count_Pairs([1, 2, 3, 4, 5, 6, 7, 8], 8), 7)

    def test_edge_case8(self):
        self.assertEqual(count_Pairs([1, 1, 1, 1, 1, 1, 1, 1], 8), 0)
