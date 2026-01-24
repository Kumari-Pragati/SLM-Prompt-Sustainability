import unittest
from mbpp_607_code import find_literals

class TestFindLiterals(unittest.TestCase):
    def test_find_literal_in_text(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog.', 'fox'), ('fox', 17, 21))

    def test_find_literal_not_in_text(self):
        self.assertEqual(find_literals('The quick brown dog jumps over the lazy fox.', 'fox'), (None, None, None))

    def test_find_literal_with_empty_text(self):
        self.assertEqual(find_literals('', 'fox'), (None, None, None))

    def test_find_literal_with_none_text(self):
        self.assertEqual(find_literals(None, 'fox'), (None, None, None))

    def test_find_literal_with_none_pattern(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog.', None), (None, None, None))
