import unittest
from mbpp_607_code import find_literals

class TestFindLiterals(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog.', 'fox'), ('fox', 16, 19))

    def test_edge_case_empty_text(self):
        self.assertEqual(find_literals('', 'fox'), None)

    def test_edge_case_empty_pattern(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog.', ''), None)

    def test_edge_case_text_contains_only_pattern(self):
        self.assertEqual(find_literals('fox', 'fox'), ('fox', 0, 3))

    def test_edge_case_pattern_not_in_text(self):
        self.assertEqual(find_literals('The quick brown dog.', 'fox'), None)

    def test_complex_case_multiple_occurrences(self):
        self.assertEqual(find_literals('fox fox fox', 'fox'), ('fox', 0, 3))

    def test_complex_case_case_insensitive_search(self):
        self.assertEqual(find_literals('The quick brown Fox jumps over the lazy Dog.', 'fox'), ('fox', 16, 19))
