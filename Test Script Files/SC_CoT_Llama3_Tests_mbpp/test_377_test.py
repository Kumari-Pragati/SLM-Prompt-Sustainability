import unittest
from mbpp_377_code import remove_Char

class TestRemoveChar(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(remove_Char("hello world", "o"), "hell wrld")

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_Char("", "a"), "")

    def test_edge_case_single_char_string(self):
        self.assertEqual(remove_Char("a", "a"), "")

    def test_edge_case_single_char_string_no_match(self):
        self.assertEqual(remove_Char("a", "b"), "a")

    def test_edge_case_single_char_string_multiple_matches(self):
        self.assertEqual(remove_Char("aa", "a"), "")

    def test_edge_case_single_char_string_no_matches(self):
        self.assertEqual(remove_Char("bc", "a"), "bc")

    def test_edge_case_single_char_string_multiple_matches_and_no_matches(self):
        self.assertEqual(remove_Char("aba", "a"), "b")

    def test_edge_case_single_char_string_multiple_matches_and_no_matches_edge(self):
        self.assertEqual(remove_Char("aabb", "a"), "bb")

    def test_edge_case_single_char_string_multiple_matches_and_no_matches_edge2(self):
        self.assertEqual(remove_Char("abc", "a"), "bc")

    def test_edge_case_single_char_string_multiple_matches_and_no_matches_edge3(self):
        self.assertEqual(remove_Char("abca", "a"), "bc")

    def test_edge_case_single_char_string_multiple_matches_and_no_matches_edge4(self):
        self.assertEqual(remove_Char("abcab", "a"), "bc")

    def test_edge_case_single_char_string_multiple_matches_and_no_matches_edge5(self):
        self.assertEqual(remove_Char("abcabc", "a"), "bc")

    def test_edge_case_single_char_string_multiple_matches_and_no_matches_edge6(self):
        self.assertEqual(remove_Char("abcabcd", "a"), "bcd")

    def test_edge_case_single_char_string_multiple_matches_and_no_matches_edge7(self):
        self.assertEqual(remove_Char("abcabcde", "a"), "bcde")

    def test_edge_case_single_char_string_multiple_matches_and_no_matches_edge8(self):
        self.assertEqual(remove_Char("abcabcdef", "a"), "bcdef")

    def test_edge_case_single_char_string_multiple_matches_and_no_matches_edge9(self):
        self.assertEqual(remove_Char("abcabcdefg", "a"), "bcdefg")

    def test_edge_case_single_char_string_multiple_matches_and_no_matches_edge10(self):
        self.assertEqual(remove_Char("abcabcdefgh", "a"), "bcdefgh")

    def test_edge_case_single_char_string_multiple_matches_and_no_matches_edge11(self):
        self.assertEqual(remove_Char("abcabcdefghi", "a"), "bcdefghi")

    def test_edge_case_single_char_string_multiple_matches_and_no_matches_edge12(self):
        self.assertEqual(remove_Char("abcabcdefghij", "a"), "bcdefghij")

    def test_edge_case_single_char_string_multiple_matches_and_no_matches_edge13(self):
        self.assertEqual(remove_Char("abcabcdefghijk", "a"), "bcdefghijk")

    def test_edge_case_single_char_string_multiple_matches_and_no_matches_edge14(self):
        self.assertEqual(remove_Char("abcabcdefghijka", "a"), "bcdefghijka")

    def test_edge_case_single_char_string_multiple_matches_and_no_matches_edge15(self):
        self.assertEqual(remove_Char("abcabcdefghijklb", "a"), "bcdefghijklb")

    def test_edge_case_single_char_string_multiple_matches_and_no_matches_edge16(self):
        self.assertEqual(remove_Char("abcabcdefghijklc", "a"), "bcdefghijklc")

    def test_edge_case_single_char_string_multiple_matches_and_no_matches_edge17(self):
        self.assertEqual(remove_Char("abcabcdefghijkl", "a"), "bcdefghijkl")

    def test_edge_case_single_char_string_multiple_matches_and_no_matches_edge18(self):
        self.assertEqual(remove_Char("abcabcdefghijlk", "a"), "bcdefghijlk")

    def test_edge_case_single_char_string_multiple_matches_and_no_matches_edge19(self):
        self.assertEqual(remove_Char("abcabcdefghijlka", "a"), "bcdefghijlka")

    def test_edge_case_single_char_string_multiple_matches_and_no_matches_edge20(self):
        self.assertEqual(remove_Char("abcabcdefghijlkab", "a"), "bcdefghijlkab")

    def test_edge_case_single_char_string_multiple_matches_and_no_matches_edge21(self):
        self.assertEqual(remove_Char("abcabcdefghijlkabc", "a"), "bcdefghijlkabc")

    def test_edge_case_single_char_string_multiple_matches_and_no_matches_edge22(self):
        self.assertEqual(remove_Char("abcabcdefghijlkabcd", "a"), "bcdefghijlkabcd")

    def test_edge_case_single_char_string_multiple_matches_and_no_matches_edge23(self):
        self.assertEqual(remove_Char("abcabcdefgh