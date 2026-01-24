import unittest
from mbpp_831_code import count_Pairs

class TestCountPairs(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_Pairs([], 0), 0)

    def test_single_element(self):
        self.assertEqual(count_Pairs([1], 1), 0)

    def test_single_pair(self):
        self.assertEqual(count_Pairs([1, 1], 2), 1)

    def test_multiple_pairs(self):
        self.assertEqual(count_Pairs([1, 1, 2, 2, 3, 3], 6), 3)

    def test_no_pairs(self):
        self.assertEqual(count_Pairs([1, 2, 3, 4, 5], 5), 0)

    def test_duplicate_index(self):
        with self.assertRaises(IndexError):
            count_Pairs([1, 2], 1)

    def test_negative_index(self):
        with self.assertRaises(IndexError):
            count_Pairs([1, 2], -1)

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            count_Pairs([1, 'a'], 2)

    def test_non_integer_length(self):
        with self.assertRaises(TypeError):
            count_Pairs([1], 'length')
