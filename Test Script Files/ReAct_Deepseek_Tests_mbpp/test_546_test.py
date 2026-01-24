import unittest
from mbpp_546_code import last_occurence_char

class TestLastOccurenceChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(last_occurence_char('hello', 'l'), 5)

    def test_edge_case_char_not_in_string(self):
        self.assertIsNone(last_occurence_char('hello', 'z'))

    def test_edge_case_empty_string(self):
        self.assertIsNone(last_occurence_char('', 'a'))

    def test_edge_case_char_at_start_of_string(self):
        self.assertEqual(last_occurence_char('hello', 'h'), 1)

    def test_edge_case_char_at_end_of_string(self):
        self.assertEqual(last_occurence_char('hello', 'o'), 6)

    def test_edge_case_single_char_string(self):
        self.assertEqual(last_occurence_char('a', 'a'), 2)
