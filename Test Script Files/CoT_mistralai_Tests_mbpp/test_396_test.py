import unittest
from mbpp_396_code import check_char

class TestCheckChar(unittest.TestCase):
    def test_valid_single_char(self):
        self.assertEqual(check_char("a"), "Valid")
        self.assertEqual(check_char("z"), "Valid")

    def test_valid_multi_char_same_as_first(self):
        self.assertEqual(check_char("aaa"), "Valid")
        self.assertEqual(check_char("zzz"), "Valid")

    def test_valid_multi_char_different_first_and_last(self):
        self.assertEqual(check_char("abab"), "Valid")
        self.assertEqual(check_char("xyxy"), "Valid")

    def test_invalid_multi_char_different_first_and_last_different_last(self):
        self.assertEqual(check_char("abcd"), "Invalid")
        self.assertEqual(check_char("xyz"), "Invalid")

    def test_invalid_non_alphabet(self):
        self.assertEqual(check_char("1"), "Invalid")
        self.assertEqual(check_char("!"), "Invalid")
        self.assertEqual(check_char("_"), "Invalid")

    def test_invalid_empty_string(self):
        self.assertEqual(check_char(""), "Invalid")

    def test_invalid_multi_char_same_but_not_at_start_and_end(self):
        self.assertEqual(check_char("aaaba"), "Invalid")
        self.assertEqual(check_char("zzzyy"), "Invalid")
