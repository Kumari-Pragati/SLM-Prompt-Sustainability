import unittest
from mbpp_290_code import max_length

class TestMaxLength(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_length(['abc', 'defgh', 'ijklm']), (5, 'defgh'))

    def test_empty_list(self):
        self.assertEqual(max_length([]), (0, ''))

    def test_single_element(self):
        self.assertEqual(max_length(['abc']), (3, 'abc'))

    def test_all_same_length(self):
        self.assertEqual(max_length(['abc', 'def', 'ghi']), (3, 'abc'))

    def test_empty_strings(self):
        self.assertEqual(max_length(['', '']), (0, ''))

    def test_whitespace_strings(self):
        self.assertEqual(max_length([' ', '   ']), (2, '   '))

    def test_numeric_strings(self):
        self.assertEqual(max_length(['123', '45678']), (5, '45678'))

    def test_mixed_numeric_and_alpha(self):
        self.assertEqual(max_length(['abc123', 'def456']), (7, 'abc123'))

    def test_special_characters(self):
        self.assertEqual(max_length(['!@#', '$%^&*']), (5, '$%^&*'))

    def test_unicode_strings(self):
        self.assertEqual(max_length(['日本語', '漢字']), (3, '漢字'))
