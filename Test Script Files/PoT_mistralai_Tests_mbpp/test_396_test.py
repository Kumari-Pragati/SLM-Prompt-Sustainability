import unittest
from mbpp_396_code import check_char

class TestCheckChar(unittest.TestCase):
    def test_valid_single_char(self):
        self.assertEqual(check_char("a"), "Valid")
        self.assertEqual(check_char("z"), "Valid")

    def test_valid_multi_char_same_char(self):
        self.assertEqual(check_char("aaa"), "Valid")
        self.assertEqual(check_char("zzz"), "Valid")

    def test_valid_multi_char_different_char_start_and_end(self):
        self.assertEqual(check_char("abcd"), "Invalid")
        self.assertEqual(check_char("xyzw"), "Invalid")

    def test_valid_multi_char_different_char_middle(self):
        self.assertEqual(check_char("axbxc"), "Valid")
        self.assertEqual(check_char("pqrst"), "Valid")

    def test_invalid_empty_string(self):
        self.assertEqual(check_char(""), "Invalid")

    def test_invalid_non_alphabet(self):
        self.assertEqual(check_char("123"), "Invalid")
        self.assertEqual(check_char("_"), "Invalid")
        self.assertEqual(check_char("!"), "Invalid")

    def test_invalid_multi_non_alphabet(self):
        self.assertEqual(check_char("1a2"), "Invalid")
        self.assertEqual(check_char("a_b"), "Invalid")
        self.assertEqual(check_char("!z"), "Invalid")
