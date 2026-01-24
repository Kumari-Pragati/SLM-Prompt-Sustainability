import unittest
from mbpp_773_code import occurance_substring

class TestOccuranceSubstring(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(occurance_substring("hello world", "world"), ("world", 6, 11))

    def test_edge_conditions(self):
        self.assertEqual(occurance_substring("", ""), ("", 0, 0))
        self.assertEqual(occurance_substring("hello world", ""), ("", 0, 0))
        self.assertIsNone(occurance_substring("hello world", "non_existent"))

    def test_complex_cases(self):
        self.assertEqual(occurance_substring("hello world, hello world", "world"), ("world", 6, 11))
        self.assertEqual(occurance_substring("hello world, hello world", "world"), ("world", 6, 11))
        self.assertEqual(occurance_substring("hello world, hello world", "world"), ("world", 6, 11))
