import unittest
from mbpp_727_code import remove_char

class TestRemoveChar(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_char("Hello_World_123"), "HelloWorld123")

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_char(""), "")

    def test_edge_case_single_char(self):
        self.assertEqual(remove_char("a"), "a")

    def test_edge_case_single_word(self):
        self.assertEqual(remove_char("Hello"), "Hello")

    def test_edge_case_all_digits(self):
        self.assertEqual(remove_char("123456"), "123456")

    def test_edge_case_all_special_characters(self):
        self.assertEqual(remove_char("!@#$%^&*()_+-="), "")

    def test_edge_case_all_whitespace(self):
        self.assertEqual(remove_char("   "), "")

    def test_corner_case_mixed_case(self):
        self.assertEqual(remove_char("HeLlO_WoRlD_123"), "HelloWorld123")

    def test_corner_case_leading_trailing_whitespace(self):
        self.assertEqual(remove_char("   HeLlO_WoRlD_123   "), "HelloWorld123")
