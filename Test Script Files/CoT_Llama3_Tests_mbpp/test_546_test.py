import unittest
from mbpp_546_code import last_occurence_char

class TestLastOccurenceChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(last_occurence_char("hello world", 'o'), 7)

    def test_edge_case_char_not_found(self):
        self.assertIsNone(last_occurence_char("hello world", 'z'))

    def test_edge_case_char_at_start(self):
        self.assertEqual(last_occurence_char("hello world", 'h'), 0)

    def test_edge_case_char_at_end(self):
        self.assertEqual(last_occurence_char("hello world", 'd'), 10)

    def test_edge_case_char_multiple_occurrences(self):
        self.assertEqual(last_occurence_char("hello world hello", 'o'), 7)

    def test_edge_case_char_multiple_occurrences_at_start(self):
        self.assertEqual(last_occurence_char("hello world hello", 'h'), 0)

    def test_edge_case_char_multiple_occurrences_at_end(self):
        self.assertEqual(last_occurence_char("hello world hello", 'd'), 10)

    def test_edge_case_empty_string(self):
        self.assertIsNone(last_occurence_char("", 'a'))

    def test_edge_case_empty_string_char_not_found(self):
        self.assertIsNone(last_occurence_char("", 'z'))

    def test_edge_case_single_char_string(self):
        self.assertEqual(last_occurence_char("a", 'a'), 0)

    def test_edge_case_single_char_string_char_not_found(self):
        self.assertIsNone(last_occurence_char("a", 'z'))
