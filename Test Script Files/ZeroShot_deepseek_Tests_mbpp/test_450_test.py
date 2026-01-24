import unittest
from mbpp_450_code import extract_string

class TestExtractString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(extract_string("", 5), [])

    def test_string_with_elements_of_different_lengths(self):
        self.assertEqual(extract_string(["abc", "defg", "hij", "klmnop", "qr"], 3), ["abc", "hij"])

    def test_string_with_elements_of_same_length(self):
        self.assertEqual(extract_string(["abc", "def", "ghi", "jkl"], 3), ["abc", "def", "ghi", "jkl"])

    def test_string_with_elements_of_longer_length(self):
        self.assertEqual(extract_string(["abcdef", "ghijklm"], 3), [])

    def test_string_with_elements_of_shorter_length(self):
        self.assertEqual(extract_string(["ab", "cde", "fghi"], 4), [])
