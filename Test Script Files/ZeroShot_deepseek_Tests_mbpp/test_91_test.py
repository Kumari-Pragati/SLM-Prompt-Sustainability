import unittest
from mbpp_91_code import find_substring

class TestFindSubstring(unittest.TestCase):

    def test_find_substring_positive(self):
        self.assertTrue(find_substring(['hello', 'world'], 'world'))
        self.assertTrue(find_substring(['hello', 'world'], 'hello'))
        self.assertTrue(find_substring(['hello', 'world', 'python'], 'python'))

    def test_find_substring_negative(self):
        self.assertFalse(find_substring(['hello', 'world'], 'java'))
        self.assertFalse(find_substring(['hello', 'world'], ''))
        self.assertFalse(find_substring([], 'python'))

    def test_find_substring_edge_cases(self):
        self.assertTrue(find_substring(['', ''], ''))
        self.assertFalse(find_substring(['', ''], 'a'))
