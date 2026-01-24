import unittest
from mbpp_528_code import min_length

class TestMinLength(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_length(['abc', 'def', 'ghi']), (3, 'abc'))

    def test_empty_list(self):
        self.assertEqual(min_length([]), (0, ''))

    def test_single_element_list(self):
        self.assertEqual(min_length(['abc']), (3, 'abc'))

    def test_all_empty_strings(self):
        self.assertEqual(min_length(['', '']), (0, ''))

    def test_all_same_length_strings(self):
        self.assertEqual(min_length(['abcd', 'abc', 'ab']), (2, 'ab'))

    def test_mixed_length_strings(self):
        self.assertEqual(min_length(['abc', 'abcdef', 'ab']), (2, 'ab'))

    def test_strings_with_whitespace(self):
        self.assertEqual(min_length(['abc def', 'ghi']), (6, 'ghi'))
