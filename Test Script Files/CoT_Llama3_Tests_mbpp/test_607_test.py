import unittest
from mbpp_607_code import find_literals

class TestFindLiterals(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog.', 'fox'), ('fox', 15, 19))

    def test_edge_case_empty_pattern(self):
        with self.assertRaises(re.error):
            find_literals('The quick brown fox jumps over the lazy dog.', '')

    def test_edge_case_empty_text(self):
        with self.assertRaises(re.error):
            find_literals('', 'fox')

    def test_edge_case_pattern_not_found(self):
        self.assertEqual(find_literals('The quick brown dog jumps over the lazy dog.', 'fox'), ('fox', None, None))

    def test_edge_case_pattern_at_start(self):
        self.assertEqual(find_literals('fox jumps over the lazy dog.', 'fox'), ('fox', 0, 3))

    def test_edge_case_pattern_at_end(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog.', 'fox'), ('fox', 15, 19))

    def test_edge_case_pattern_multiple_occurrences(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy fox dog.', 'fox'), ('fox', 15, 19))

    def test_edge_case_pattern_with_spaces(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog.','brown fox'), (' brown fox', 15, 19))

    def test_edge_case_pattern_with_punctuation(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog.,', 'fox'), ('fox', 15, 19))
