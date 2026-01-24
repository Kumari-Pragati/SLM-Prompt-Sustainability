import unittest
from mbpp_757_code import count_reverse_pairs

class TestCountReversePairs(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_reverse_pairs([1, 2, 3]), '3')

    def test_edge_case_empty_list(self):
        self.assertEqual(count_reverse_pairs([]), '0')

    def test_edge_case_single_element_list(self):
        self.assertEqual(count_reverse_pairs([1]), '0')

    def test_edge_case_single_element_list_with_match(self):
        self.assertEqual(count_reverse_pairs(['a']), '1')

    def test_edge_case_single_element_list_with_no_match(self):
        self.assertEqual(count_reverse_pairs(['b']), '0')

    def test_edge_case_list_with_single_match(self):
        self.assertEqual(count_reverse_pairs([1, 2, 3, 3]), '1')

    def test_edge_case_list_with_multiple_matches(self):
        self.assertEqual(count_reverse_pairs([1, 2, 3, 3, 3]), '3')

    def test_edge_case_list_with_no_matches(self):
        self.assertEqual(count_reverse_pairs([1, 2, 3, 4]), '0')

    def test_edge_case_list_with_duplicates(self):
        self.assertEqual(count_reverse_pairs([1, 2, 2, 3, 3, 3]), '3')

    def test_edge_case_list_with_duplicates_and_matches(self):
        self.assertEqual(count_reverse_pairs([1, 2, 2, 3, 3, 3, 3]), '4')
