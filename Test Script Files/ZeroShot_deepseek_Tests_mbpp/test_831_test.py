import unittest
from mbpp_831_code import count_Pairs

class TestCountPairs(unittest.TestCase):

    def test_count_Pairs_with_positive_integers(self):
        self.assertEqual(count_Pairs([1, 2, 3, 2, 1], 5), 2)

    def test_count_Pairs_with_negative_integers(self):
        self.assertEqual(count_Pairs([-1, -2, -3, -2, -1], 5), 2)

    def test_count_Pairs_with_mixed_integers(self):
        self.assertEqual(count_Pairs([1, -2, 3, -2, 1], 5), 2)

    def test_count_Pairs_with_single_element(self):
        self.assertEqual(count_Pairs([1], 1), 0)

    def test_count_Pairs_with_empty_list(self):
        self.assertEqual(count_Pairs([], 0), 0)
