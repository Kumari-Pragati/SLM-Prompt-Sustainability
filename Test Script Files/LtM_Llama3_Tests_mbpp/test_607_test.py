import unittest
from mbpp_607_code import find_literals

class TestFindLiterals(unittest.TestCase):
    def test_simple_match(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog.', 'fox'), ('fox', 15, 19))

    def test_no_match(self):
        self.assertIsNone(find_literals('The quick brown dog jumps over the lazy dog.', 'fox'))

    def test_empty_pattern(self):
        self.assertIsNone(find_literals('The quick brown fox jumps over the lazy dog.', ''))

    def test_empty_text(self):
        self.assertIsNone(find_literals('', 'fox'))

    def test_pattern_not_found(self):
        self.assertIsNone(find_literals('The quick brown dog jumps over the lazy dog.', 'elephant'))

    def test_pattern_found_at_start(self):
        self.assertEqual(find_literals('fox jumps over the lazy dog.', 'fox'), ('fox', 0, 3))

    def test_pattern_found_at_end(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog.', 'fox'), ('fox', 15, 19))

    def test_pattern_found_multiple_times(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy fox dog.', 'fox'), ('fox', 15, 19))
