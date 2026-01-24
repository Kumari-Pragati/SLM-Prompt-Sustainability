import unittest
from mbpp_450_code import extract_string

class TestExtractString(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(extract_string("abcdefg", 3), ["abc", "def"])
        self.assertEqual(extract_string("1234567", 4), ["1234", "2345", "3456"])

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(extract_string("", 1), [])
        self.assertEqual(extract_string("a", 1), ["a"])
        self.assertEqual(extract_string("aa", 1), ["a"])
        self.assertEqual(extract_string("aaa", 1), ["a"])
        self.assertEqual(extract_string("aaaa", 1), ["a"])
        self.assertEqual(extract_string("aaaa", 2), ["aa"])
        self.assertEqual(extract_string("aaaa", 3), ["aaa"])
        self.assertEqual(extract_string("aaaa", 4), ["aaaa"])

    def test_empty_string_in_list(self):
        self.assertEqual(extract_string("abcdefg", 0), [])
        self.assertEqual(extract_string("abcdefg", 5), [])

    def test_invalid_input(self):
        self.assertRaises(ValueError, extract_string, "abc", 0)
        self.assertRaises(ValueError, extract_string, "abc", -1)
        self.assertRaises(ValueError, extract_string, "", 1)
        self.assertRaises(ValueError, extract_string, "a", 0)
