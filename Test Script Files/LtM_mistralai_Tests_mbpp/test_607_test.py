import unittest
from mbpp_607_code import find_literals

class TestFindLiterals(unittest.TestCase):

    def test_simple_match(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog.', 'fox'), ('fox', 23, 28))

    def test_case_insensitive_match(self):
        self.assertEqual(find_literals('THE QUICK BROWN FOX jumps over the lazy dog.', 'fox'), ('fox', 23, 28))

    def test_no_match(self):
        self.assertEqual(find_literals('The quick brown dog jumps over the lazy fox.', 'fox'), (None, None, None))

    def test_empty_input(self):
        self.assertEqual(find_literals('', 'fox'), (None, None, None))

    def test_single_character_pattern(self):
        self.assertEqual(find_literals('a', 'a'), ('a', 0, 1))

    def test_multi_word_text(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog and the cat.', 'fox'), ('fox', 23, 28))

    def test_multiple_matches(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the quick brown fox.', 'fox'), ('fox', 23, 28))
