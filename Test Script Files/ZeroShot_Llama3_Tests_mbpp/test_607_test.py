import unittest
from mbpp_607_code import find_literals

class TestFindLiterals(unittest.TestCase):

    def test_find_literals(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog.', 'fox'), ('fox', 15, 19))

    def test_find_literals_no_match(self):
        self.assertIsNone(find_literals('The quick brown dog jumps over the lazy dog.', 'fox'))

    def test_find_literals_empty_string(self):
        self.assertIsNone(find_literals('', 'fox'))

    def test_find_literals_pattern_empty_string(self):
        self.assertIsNone(find_literals('The quick brown dog jumps over the lazy dog.', ''))

    def test_find_literals_pattern_none(self):
        self.assertIsNone(find_literals('The quick brown dog jumps over the lazy dog.', None))
