import unittest
from mbpp_144_code import sum_Pairs

class TestSumPairs(unittest.TestCase):
    def test_sum_Pairs_typical(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4, 5], 5), 15)

    def test_sum_Pairs_edge(self):
        self.assertEqual(sum_Pairs([1, 2, 3], 3), 3)

    def test_sum_Pairs_edge2(self):
        self.assertEqual(sum_Pairs([1, 2], 2), 1)

    def test_sum_Pairs_edge3(self):
        self.assertEqual(sum_Pairs([1], 1), 0)

    def test_sum_Pairs_invalid(self):
        with self.assertRaises(TypeError):
            sum_Pairs("abc", 5)

    def test_sum_Pairs_invalid2(self):
        with self.assertRaises(TypeError):
            sum_Pairs([1, 2, 3], "abc")
