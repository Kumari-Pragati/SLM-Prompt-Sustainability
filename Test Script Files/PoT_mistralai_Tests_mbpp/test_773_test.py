import unittest
from mbpp_773_code import occurance_substring

class TestOccurrenceSubstring(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(occurrence_substring("hello world", "world"), ("world", 6, 11))
        self.assertEqual(occurrence_substring("Python is a great language", "Python", 0), ("Python", 0, 6))
        self.assertEqual(occurrence_substring("aaabbbccc", "bbb"), ("bbb", 2, 5))

    def test_edge_cases(self):
        self.assertEqual(occurrence_substring("", "x"), (None, None, None))
        self.assertEqual(occurrence_substring("x", "x"), ("x", 0, 1))
        self.assertEqual(occurrence_substring("xx", "x"), ("x", 0, 1))
        self.assertEqual(occurrence_substring("xx", "xx"), ("xx", 0, 2))
        self.assertEqual(occurrence_substring("abc", "abcdef"), (None, None, None))
        self.assertEqual(occurrence_substring("abc", ""), (None, None, None))
        self.assertEqual(occurrence_substring("abc", "a"), ("a", 0, 1))
        self.assertEqual(occurrence_substring("abc", "c"), ("c", 2, 3))
        self.assertEqual(occurrence_substring("abc", "d"), (None, None, None))

    def test_boundary_cases(self):
        self.assertEqual(occurrence_substring("hello world", "world\n"), ("world", 6, 11))
        self.assertEqual(occurrence_substring("hello world", "\nworld"), (None, None, None))
        self.assertEqual(occurrence_substring("hello world", "\n"), (None, None, None))
        self.assertEqual(occurrence_substring("hello world", "world\nworld"), ("world", 6, 11))
        self.assertEqual(occurrence_substring("hello world", "worldworld"), (None, None, None))
        self.assertEqual(occurrence_substring("hello world", "worldworld\n"), ("worldworld", 6, 22))
