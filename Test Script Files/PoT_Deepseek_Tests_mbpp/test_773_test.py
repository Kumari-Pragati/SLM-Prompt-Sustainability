import unittest
from mbpp_773_code import occurance_substring

class TestOccuranceSubstring(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(occurance_substring("Hello, world!", "world"), ("world", 7, 12))

    def test_edge_case_empty_string(self):
        self.assertEqual(occurance_substring("", "world"), None)

    def test_boundary_case_at_start(self):
        self.assertEqual(occurance_substring("world! Hello,", "world"), ("world", 0, 5))

    def test_boundary_case_at_end(self):
        self.assertEqual(occurance_substring("Hello, world!", "!"), ("!", 12, 13))

    def test_corner_case_repeated_substring(self):
        self.assertEqual(occurance_substring("Hello, world! world", "world"), ("world", 7, 12))

    def test_corner_case_substring_not_found(self):
        self.assertIsNone(occurance_substring("Hello, world!", "python"))
