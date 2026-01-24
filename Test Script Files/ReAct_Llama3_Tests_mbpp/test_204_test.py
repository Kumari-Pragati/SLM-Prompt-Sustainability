import unittest
from mbpp_204_code import count

class TestCountFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count("hello world", 'o'), 2)

    def test_edge_case_empty_string(self):
        self.assertEqual(count("", 'a'), 0)

    def test_edge_case_single_char_string(self):
        self.assertEqual(count("a", 'a'), 1)

    def test_edge_case_single_char_string_no_match(self):
        self.assertEqual(count("a", 'b'), 0)

    def test_edge_case_single_char_string_all_matches(self):
        self.assertEqual(count("a", 'a'), 1)

    def test_edge_case_single_char_string_all_matches_multiple(self):
        self.assertEqual(count("aaa", 'a'), 3)

    def test_edge_case_single_char_string_no_matches(self):
        self.assertEqual(count("abc", 'd'), 0)

    def test_edge_case_single_char_string_all_matches_multiple(self):
        self.assertEqual(count("abc", 'a'), 1)

    def test_edge_case_single_char_string_all_matches_multiple(self):
        self.assertEqual(count("abc", 'b'), 1)

    def test_edge_case_single_char_string_all_matches_multiple(self):
        self.assertEqual(count("abc", 'c'), 1)

    def test_edge_case_single_char_string_all_matches_multiple(self):
        self.assertEqual(count("abc", 'd'), 0)

    def test_edge_case_single_char_string_all_matches_multiple(self):
        self.assertEqual(count("abc", 'e'), 0)

    def test_edge_case_single_char_string_all_matches_multiple(self):
        self.assertEqual(count("abc", 'f'), 0)

    def test_edge_case_single_char_string_all_matches_multiple(self):
        self.assertEqual(count("abc", 'g'), 0)

    def test_edge_case_single_char_string_all_matches_multiple(self):
        self.assertEqual(count("abc", 'h'), 0)

    def test_edge_case_single_char_string_all_matches_multiple(self):
        self.assertEqual(count("abc", 'i'), 0)

    def test_edge_case_single_char_string_all_matches_multiple(self):
        self.assertEqual(count("abc", 'j'), 0)

    def test_edge_case_single_char_string_all_matches_multiple(self):
        self.assertEqual(count("abc", 'k'), 0)

    def test_edge_case_single_char_string_all_matches_multiple(self):
        self.assertEqual(count("abc", 'l'), 0)

    def test_edge_case_single_char_string_all_matches_multiple(self):
        self.assertEqual(count("abc",'m'), 0)

    def test_edge_case_single_char_string_all_matches_multiple(self):
        self.assertEqual(count("abc", 'n'), 0)

    def test_edge_case_single_char_string_all_matches_multiple(self):
        self.assertEqual(count("abc", 'o'), 0)

    def test_edge_case_single_char_string_all_matches_multiple(self):
        self.assertEqual(count("abc", 'p'), 0)

    def test_edge_case_single_char_string_all_matches_multiple(self):
        self.assertEqual(count("abc", 'q'), 0)

    def test_edge_case_single_char_string_all_matches_multiple(self):
        self.assertEqual(count("abc", 'r'), 0)

    def test_edge_case_single_char_string_all_matches_multiple(self):
        self.assertEqual(count("abc",'s'), 0)

    def test_edge_case_single_char_string_all_matches_multiple(self):
        self.assertEqual(count("abc", 't'), 0)

    def test_edge_case_single_char_string_all_matches_multiple(self):
        self.assertEqual(count("abc", 'u'), 0)

    def test_edge_case_single_char_string_all_matches_multiple(self):
        self.assertEqual(count("abc", 'v'), 0)

    def test_edge_case_single_char_string_all_matches_multiple(self):
        self.assertEqual(count("abc", 'w'), 0)

    def test_edge_case_single_char_string_all_matches_multiple(self):
        self.assertEqual(count("abc", 'x'), 0)

    def test_edge_case_single_char_string_all_matches_multiple(self):
        self.assertEqual(count("abc", 'y'), 0)

    def test_edge_case_single_char_string_all_matches_multiple(self):
        self.assertEqual(count("abc", 'z'), 0)

    def test_edge_case_single_char_string_all_matches_multiple(self):
        self.assertEqual(count("abc", 'a'), 1)

    def test_edge_case_single_char_string_all_matches_multiple(self):
        self.assertEqual(count("abc", 'b'), 1)

    def test_edge_case_single_char_string_all_matches_multiple(self):
        self.assertEqual(count("abc", 'c'), 1)

    def test_edge_case_single_char_string_all_matches_multiple(self):
        self.assertEqual(count("abc", 'd'), 0)

    def test_edge_case_single_char_string_all_matches_multiple(self):
        self.assertEqual(count("abc", 'e'), 0)

    def test_edge_case_single_char_string_all_matches_multiple(self):
        self.assertEqual(count("abc", 'f'), 0)

    def test_edge_case_single_char