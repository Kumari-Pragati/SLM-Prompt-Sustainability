import unittest
from mbpp_53_code import check_Equality

class TestCheckEquality(unittest.TestCase):
    def test_equal_string(self):
        self.assertEqual(check_Equality("abcd"), "Equal")

    def test_empty_string(self):
        self.assertEqual(check_Equality(""), "Equal")

    def test_single_character_string(self):
        self.assertEqual(check_Equality("a"), "Equal")

    def test_reverse_string(self):
        self.assertEqual(check_Equality("coda"), "Equal")

    def test_mixed_case_string(self):
        self.assertEqual(check_Equality("AbCd"), "Not Equal")

    def test_string_with_special_characters(self):
        self.assertEqual(check_Equality("Ab12Cd"), "Not Equal")
