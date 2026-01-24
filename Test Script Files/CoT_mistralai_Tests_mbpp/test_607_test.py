import unittest
from mbpp_607_code import find_literals

class TestFindLiterals(unittest.TestCase):
    def test_find_literals_with_match(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog.', 'fox'), ('fox', 17, 21))
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy fox.', 'fox'), ('fox', 17, 23))

    def test_find_literals_no_match(self):
        self.assertIsNone(find_literals('The quick brown dog jumps over the lazy dog.', 'fox'))
        self.assertIsNone(find_literals('The quick brown fox jumps over the lazy fox.', 'lion'))

    def test_find_literals_empty_string(self):
        self.assertIsNone(find_literals('', 'fox'))

    def test_find_literals_single_char_pattern(self):
        self.assertEqual(find_literals('a', 'a'), ('a', 0, 1))
        self.assertIsNone(find_literals('b', 'a'))

    def test_find_literals_case_sensitivity(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog.', 'fox'), ('fox', 17, 21))
        self.assertIsNone(find_literals('The quick brown fox jumps over the lazy dog.', 'Fox'))
