import unittest
from mbpp_773_code import occurance_substring

class TestOccuranceSubstring(unittest.TestCase):

    def test_typical_case(self):
        text = "Hello, World!"
        pattern = "World"
        result = occurance_substring(text, pattern)
        self.assertEqual(result, ("World", 7, 12))

    def test_edge_case_no_match(self):
        text = "Hello, World!"
        pattern = "Python"
        result = occurance_substring(text, pattern)
        self.assertIsNone(result)

    def test_edge_case_empty_text(self):
        text = ""
        pattern = "World"
        result = occurance_substring(text, pattern)
        self.assertIsNone(result)

    def test_edge_case_empty_pattern(self):
        text = "Hello, World!"
        pattern = ""
        result = occurance_substring(text, pattern)
        self.assertIsNone(result)

    def test_edge_case_pattern_longer_than_text(self):
        text = "Hello"
        pattern = "Hello, World!"
        result = occurance_substring(text, pattern)
        self.assertIsNone(result)

    def test_typical_case_with_spaces(self):
        text = "This is a test string"
        pattern = "test"
        result = occurance_substring(text, pattern)
        self.assertEqual(result, ("test", 10, 14))

    def test_typical_case_with_special_chars(self):
        text = "This is a @test string!"
        pattern = "@test"
        result = occurance_substring(text, pattern)
        self.assertEqual(result, ("@test", 10, 15))
