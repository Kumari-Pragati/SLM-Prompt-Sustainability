import unittest
from mbpp_607_code import find_literals

class TestFindLiterals(unittest.TestCase):

    def test_find_literal_in_text(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog.', 'fox'), ('fox', 22, 25))

    def test_find_literal_not_in_text(self):
        self.assertEqual(find_literals('The quick brown dog jumps over the lazy fox.', 'fox'), (None, None, None))

    def test_find_literal_empty_text(self):
        self.assertEqual(find_literals('', 'fox'), (None, None, None))

    def test_find_literal_empty_pattern(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog.', ''), (None, None, None))

    def test_find_literal_single_character(self):
        self.assertEqual(find_literals('a', 'a'), ('a', 0, 1))

    def test_find_literal_case_insensitive(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog.', 'fox'), ('fox', 22, 25))
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog.', 'Fox'), ('fox', 22, 25))

    def test_find_literal_multiple_occurrences(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy fox.', 'fox'), ('fox', 22, 25))
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy fox.', 'fox', 2), ('fox', 42, 45))

    def test_find_literal_at_boundary(self):
        self.assertEqual(find_literals('The quick brown foxjumps over the lazy dog.', 'fox'), ('fox', 0, 5))
        self.assertEqual(find_literals('The quick brown foxjumps over the lazy dog.', 'jumps'), ('jumps', 10, 17))
