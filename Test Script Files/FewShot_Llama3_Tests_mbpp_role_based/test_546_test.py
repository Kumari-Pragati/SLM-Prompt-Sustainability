import unittest
from mbpp_546_code import last_occurence_char

class TestLastOccurenceChar(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(last_occurence_char("hello", "l"), 3)

    def test_edge_case_char_not_found(self):
        self.assertIsNone(last_occurence_char("hello", "z"))

    def test_edge_case_char_at_start(self):
        self.assertEqual(last_occurence_char("hello", "h"), 0)

    def test_edge_case_char_at_end(self):
        self.assertEqual(last_occurence_char("hello", "o"), 4)

    def test_edge_case_char_multiple_occurrences(self):
        self.assertEqual(last_occurence_char("hellohello", "l"), 6)

    def test_edge_case_char_single_occurrence(self):
        self.assertEqual(last_occurence_char("hello", "o"), 4)
