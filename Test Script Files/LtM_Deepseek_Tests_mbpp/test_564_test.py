import unittest
from mbpp_564_code import count_Pairs

class TestCountPairs(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(count_Pairs([1, 2, 3, 4], 4), 3)

    def test_edge_conditions(self):
        self.assertEqual(count_Pairs([], 0), 0)
        self.assertEqual(count_Pairs([1], 1), 0)
        self.assertEqual(count_Pairs([1, 1, 1, 1], 4), 0)

    def test_complex_cases(self):
        self.assertEqual(count_Pairs([1, 2, 2, 3, 3, 4, 4, 5], 8), 8)
        self.assertEqual(count_Pairs([1, 1, 2, 2, 3, 3], 6), 6)
        self.assertEqual(count_Pairs([1, 2, 3, 4, 5, 6], 6), 15)
