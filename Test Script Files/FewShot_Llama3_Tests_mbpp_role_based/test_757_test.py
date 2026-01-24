import unittest
from mbpp_757_code import count_reverse_pairs

class TestCountReversePairs(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_reverse_pairs([]), '0')

    def test_single_element_list(self):
        self.assertEqual(count_reverse_pairs(['a']), '0')

    def test_list_with_no_reverse_pairs(self):
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c']), '0')

    def test_list_with_one_reverse_pair(self):
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c', 'c', 'a']), '1')

    def test_list_with_multiple_reverse_pairs(self):
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c', 'c', 'a', 'd', 'd', 'a']), '2')

    def test_list_with_duplicates(self):
        self.assertEqual(count_reverse_pairs(['a', 'a', 'b', 'b', 'c', 'c']), '3')

    def test_list_with_non_string_elements(self):
        self.assertEqual(count_reverse_pairs([1, 2, 3, 3, 1]), '1')

    def test_list_with_mixed_types(self):
        self.assertEqual(count_reverse_pairs(['a', 1, 'b', 'c', 'c', 'a']), '2')
