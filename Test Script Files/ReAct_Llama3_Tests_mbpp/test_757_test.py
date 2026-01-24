import unittest
from mbpp_757_code import count_reverse_pairs

class TestCountReversePairs(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_reverse_pairs([]), '0')

    def test_single_element_list(self):
        self.assertEqual(count_reverse_pairs(['a']), '0')

    def test_single_reverse_pair_list(self):
        self.assertEqual(count_reverse_pairs(['a', 'a']), '1')

    def test_multiple_reverse_pairs_list(self):
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c', 'b', 'a']), '2')

    def test_no_reverse_pairs_list(self):
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c', 'd']), '0')

    def test_duplicates_list(self):
        self.assertEqual(count_reverse_pairs(['a', 'a', 'b', 'b', 'c', 'c']), '3')

    def test_long_list(self):
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']), '0')
