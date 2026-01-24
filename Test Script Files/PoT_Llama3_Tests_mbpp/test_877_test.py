import unittest
from mbpp_877_code import sort_String

class TestSortString(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sort_String("hello"), "ehllo")

    def test_edge_case_lowercase(self):
        self.assertEqual(sort_String("abc"), "abc")

    def test_edge_case_uppercase(self):
        self.assertEqual(sort_String("ABC"), "ABC")

    def test_edge_case_mixed(self):
        self.assertEqual(sort_String("Abc"), "Abc")

    def test_edge_case_empty(self):
        self.assertEqual(sort_String(""), "")

    def test_edge_case_single_char(self):
        self.assertEqual(sort_String("a"), "a")

    def test_edge_case_all_duplicates(self):
        self.assertEqual(sort_String("aaa"), "aaa")

    def test_edge_case_all_unique(self):
        self.assertEqual(sort_String("abc"), "abc")

    def test_edge_case_all_duplicates_sorted(self):
        self.assertEqual(sort_String("aaa"), "aaa")

    def test_edge_case_all_unique_sorted(self):
        self.assertEqual(sort_String("abc"), "abc")
