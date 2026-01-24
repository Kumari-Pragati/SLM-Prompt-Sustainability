import unittest
from mbpp_144_code import sum_Pairs

class TestSumPairs(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4, 5], 5), 15)

    def test_edge_case(self):
        self.assertEqual(sum_Pairs([1, 2, 3], 3), 0)

    def test_edge_case2(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4], 4), 0)

    def test_edge_case3(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4, 5, 6], 6), 0)

    def test_edge_case4(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4, 5, 6, 7], 7), 0)

    def test_edge_case5(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4, 5, 6, 7, 8], 8), 0)

    def test_edge_case6(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 0)

    def test_edge_case7(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 0)

    def test_edge_case8(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 11), 0)

    def test_edge_case9(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 12), 0)

    def test_edge_case10(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 13), 0)

    def test_edge_case11(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 14), 0)

    def test_edge_case12(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 15), 0)

    def test_edge_case13(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 16), 0)

    def test_edge_case14(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 17), 0)

    def test_edge_case15(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], 18), 0)

    def test_edge_case16(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 19), 0)

    def test_edge_case17(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 20), 0)

    def test_edge_case18(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4