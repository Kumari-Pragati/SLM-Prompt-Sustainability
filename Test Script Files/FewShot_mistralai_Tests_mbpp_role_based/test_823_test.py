import unittest
from mbpp_823_code import check_substring

class TestCheckSubstring(unittest.TestCase):
    def test_substring_present_at_start(self):
        self.assertEqual(check_substring("StartWithMe", "Start"), "string starts with the given substring")

    def test_substring_present_in_middle(self):
        self.assertEqual(check_substring("MeInTheMiddle", "Me"), "string starts with the given substring")

    def test_substring_present_at_end(self):
        self.assertEqual(check_substring("EndsWithMe", "End"), "string starts with the given substring")

    def test_substring_not_present(self):
        self.assertEqual(check_substring("NoSubstringHere", "Substring"), "entered string isnt a substring")

    def test_empty_string(self):
        self.assertEqual(check_substring("", "Substring"), "entered string isnt a substring")

    def test_single_character_string(self):
        self.assertEqual(check_substring("A", "A"), "string starts with the given substring")
        self.assertEqual(check_substring("A", "B"), "entered string isnt a substring")
