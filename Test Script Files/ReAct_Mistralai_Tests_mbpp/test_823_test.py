import unittest
from mbpp_823_code import check_substring

class TestCheckSubscription(unittest.TestCase):

    def test_substring_present_at_start(self):
        self.assertEqual(check_substring("StartWithMe", "Start"), "string starts with the given substring")

    def test_substring_present_middle(self):
        self.assertEqual(check_substring("MeInTheMiddle", "Me"), "string starts with the given substring")

    def test_substring_present_end(self):
        self.assertEqual(check_substring("EndsWithMe", "End"), "string starts with the given substring")

    def test_substring_not_present(self):
        self.assertEqual(check_substring("NoSubstring", "Sub"), "entered string isnt a substring")

    def test_empty_string(self):
        self.assertEqual(check_substring("", "Any"), "entered string isnt a substring")

    def test_single_char_string(self):
        self.assertEqual(check_substring("A", "A"), "string starts with the given substring")
        self.assertEqual(check_substring("A", "B"), "entered string isnt a substring")

    def test_sample_empty_string(self):
        self.assertEqual(check_substring("Sample", ""), "entered string isnt a substring")

    def test_sample_single_char(self):
        self.assertEqual(check_substring("Sample", "S"), "entered string isnt a substring")
        self.assertEqual(check_substring("Sample", "a"), "entered string isnt a substring")
