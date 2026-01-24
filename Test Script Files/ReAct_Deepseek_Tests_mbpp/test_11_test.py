import unittest
from mbpp_11_code import remove_Occ

class TestRemoveOcc(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_Occ("hello", "l"), "heo")

    def test_edge_case_single_char(self):
        self.assertEqual(remove_Occ("a", "a"), "")

    def test_edge_case_no_occurrence(self):
        self.assertEqual(remove_Occ("hello", "z"), "hello")

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_Occ("", "a"), "")

    def test_edge_case_repeated_char(self):
        self.assertEqual(remove_Occ("aabbcc", "b"), "aac")

    def test_edge_case_multiple_occurrences(self):
        self.assertEqual(remove_Occ("hello world", "l"), "heo word")
