import unittest
from mbpp_546_code import last_occurence_char

class TestLastOccurenceChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(last_occurence_char("hello", 'o'), 3)

    def test_edge_case_start(self):
        self.assertEqual(last_occurence_char("hello", 'h'), 0)

    def test_edge_case_end(self):
        self.assertEqual(last_occurence_char("hello", 'o'), 3)

    def test_edge_case_not_found(self):
        self.assertIsNone(last_occurence_char("hello", 'z'))

    def test_edge_case_empty_string(self):
        self.assertIsNone(last_occurence_char("", 'a'))

    def test_edge_case_empty_char(self):
        self.assertIsNone(last_occurence_char("hello", ''))

    def test_edge_case_single_char(self):
        self.assertEqual(last_occurence_char("a", 'a'), 1)

    def test_edge_case_single_char_not_found(self):
        self.assertIsNone(last_occurence_char("a", 'b'))
