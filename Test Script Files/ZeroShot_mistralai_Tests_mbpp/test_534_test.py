import unittest
from mbpp_534_code import search_literal

class TestSearchLiteral(unittest.TestCase):

    def test_search_literal_empty_string(self):
        self.assertIsNone(search_literal('', ''))

    def test_search_literal_no_match(self):
        self.assertIsNone(search_literal('abc', 'def'))

    def test_search_literal_single_match(self):
        self.assertEqual(search_literal('ab', 'abc'), (1, 2))

    def test_search_literal_multiple_matches(self):
        self.assertEqual(search_literal('ab', 'abcdab'), [(1, 2), (5, 6)])

    def test_search_literal_case_insensitive(self):
        self.assertEqual(search_literal('Ab', 'abcAbc'), [(2, 3)])

    def test_search_literal_start_of_string(self):
        self.assertEqual(search_literal('ab', 'abcd'), (1, 2))

    def test_search_literal_end_of_string(self):
        self.assertEqual(search_literal('ab', 'cdab'), (3, 4))
