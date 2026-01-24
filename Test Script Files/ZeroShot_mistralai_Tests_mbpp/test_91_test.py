import unittest
from mbpp_91_code import find_substring

class TestFindSubstring(unittest.TestCase):

    def test_empty_string(self):
        self.assertFalse(find_substring("", "test"))

    def test_no_match(self):
        self.assertFalse(find_substring("Hello World", "Goodbye"))

    def test_case_insensitive_match(self):
        self.assertTrue(find_substring("HeLlO wOrLd", "hello"))

    def test_multiple_matches(self):
        self.assertTrue(find_substring("Hello World Hello Again", "Hello"))

    def test_match_at_start(self):
        self.assertTrue(find_substring("Hello World", "Hello"))

    def test_match_at_end(self):
        self.assertTrue(find_substring("Hello World", "World"))

    def test_match_in_middle(self):
        self.assertTrue(find_substring("Hello World", "World"))
