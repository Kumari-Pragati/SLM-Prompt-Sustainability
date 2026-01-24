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
        self.assertEqual(count_Pairs([1, 2, 2, 3, 3, 3], 6), 3)

    def test_all_duplicates(self):
        self.assertEqual(count_Pairs([1, 1, 1, 1, 1, 1], 6), 0)

    def test_negative_numbers(self):
        self.assertEqual(count_Pairs([-1, -2, 3, 4], 4), 3)

    def test_negative_and_positive_numbers(self):
        self.assertEqual(count_Pairs([-1, -2, 3, 4, 5], 5), 4)
