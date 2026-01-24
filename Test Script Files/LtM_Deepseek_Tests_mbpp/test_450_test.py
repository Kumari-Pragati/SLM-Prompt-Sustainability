import unittest
from mbpp_450_code import extract_string

class TestExtractString(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(extract_string(["abc", "def"], 3), ["abc", "def"])

    def test_empty_input(self):
        self.assertEqual(extract_string([], 3), [])

    def test_string_with_length_l(self):
        self.assertEqual(extract_string(["abc", "de", "fgh"], 3), ["abc"])

    def test_string_without_length_l(self):
        self.assertEqual(extract_string(["abc", "de", "fgh"], 2), ["de"])

    def test_multiple_strings_with_length_l(self):
        self.assertEqual(extract_string(["abc", "def", "ghi", "jkl"], 3), ["abc", "def", "ghi"])

    def test_multiple_strings_without_length_l(self):
        self.assertEqual(extract_string(["abc", "def", "ghi", "jkl"], 2), ["de", "gh"])

    def test_special_characters(self):
        self.assertEqual(extract_string(["a!b@c#", "d$e%f^"], 6), ["a!b@c#"])

    def test_maximum_length(self):
        self.assertEqual(extract_string(["abcdefgh", "ijklmnop"], 8), ["abcdefgh", "ijklmnop"])

    def test_minimum_length(self):
        self.assertEqual(extract_string(["a", "b", "c"], 1), ["a", "b", "c"])
