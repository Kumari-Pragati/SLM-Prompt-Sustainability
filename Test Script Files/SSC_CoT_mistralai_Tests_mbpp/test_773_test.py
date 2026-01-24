import unittest
from mbpp_773_code import occurance_substring

class TestOccurrenceSubstring(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(occurrence_substring("hello world", "world"), ("world", 6, 11))
        self.assertEqual(occurrence_substring("Python is awesome", "Python"), ("Python", 0, 6))

    def test_edge_and_boundary_cases(self):
        self.assertEqual(occurrence_substring("", ""), (None, None, None))
        self.assertEqual(occurrence_substring("abc", "d"), (None, None, None))
        self.assertEqual(occurrence_substring("abc", "a"), ("a", 0, 1))
        self.assertEqual(occurrence_substring("abc", "bc"), ("bc", 1, 2))
        self.assertEqual(occurrence_substring("abc", "ab"), (None, None, None))
        self.assertEqual(occurrence_substring("abc", "c"), ("c", 2, 3))
        self.assertEqual(occurrence_substring("abc", "abcd"), (None, None, None))

    def test_multiple_occurrences(self):
        self.assertEqual(occurrence_substring("aaabbc", "abb"), (("abb", 1, 4), ("abb", 5, 8)))

    def test_case_insensitive(self):
        self.assertEqual(occurrence_substring("Hello World", "world"), ("world", 6, 11))
        self.assertEqual(occurrence_substring("PyThOn Is AwEsOmE", "Python"), ("Python", 0, 6))

    def test_error_handling(self):
        self.assertRaises(TypeError, occurance_substring, 123, "pattern")
        self.assertRaises(TypeError, occurance_substring, "text", 123)
