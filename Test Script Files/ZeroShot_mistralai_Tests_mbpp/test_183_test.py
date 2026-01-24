import unittest
from mbpp_183_code import count_pairs

class TestCountPairs(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_pairs([], 0, 0), 0)

    def test_single_element(self):
        self.assertEqual(count_pairs([1], 1, 0), 0)
        self.assertEqual(count_pairs([1], 1, 1), 0)

    def test_simple_case(self):
        self.assertEqual(count_pairs([1, 2, 3, 4], 4, 5), 0)
        self.assertEqual(count_pairs([1, 2, 3, 4], 4, 2), 2)

    def test_negative_numbers(self):
        self.assertEqual(count_pairs([-1, -2, -3, -4], 4, 5), 0)
        self.assertEqual(count_pairs([-1, -2, -3, -4], 4, -1), 4)

    def test_duplicates(self):
        self.assertEqual(count_pairs([1, 1, 2, 3], 4, 0), 1)
        self.assertEqual(count_pairs([1, 1, 2, 3], 4, 2), 1)

    def test_large_numbers(self):
        self.assertEqual(count_pairs([1000, 2000, 3000, 4000], 4, 1000), 1)
        self.assertEqual(count_pairs([1000, 2000, 3000, 4000], 4, 2000), 3)
