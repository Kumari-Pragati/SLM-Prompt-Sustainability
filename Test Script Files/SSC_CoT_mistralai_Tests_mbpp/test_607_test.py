import unittest
from mbpp_607_code import Pattern
from 607_code import find_literals

class TestFindLiterals(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog.', 'fox'), (Pattern('fox'), 18, 22))

    def test_edge_case_short_text(self):
        self.assertEqual(find_literals('The quick brown fox', 'fox'), None)

    def test_edge_case_long_text(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.', 'fox'), (Pattern('fox'), 18, 22))

    def test_edge_case_multiple_matches(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the quick brown fox.', 'fox'), (Pattern('fox'), 1, 4))
        self.assertEqual(find_literals('The quick brown fox jumps over the quick brown fox.', 'brown'), (Pattern('brown'), 4, 10))

    def test_edge_case_case_insensitive(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog.', 'fox', re.IGNORECASE), (Pattern('fox', re.IGNORECASE), 18, 22))

    def test_edge_case_empty_pattern(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog.', ''), None)

    def test_edge_case_empty_text(self):
        self.assertEqual(find_literals('', 'fox'), None)

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            find_literals(1, 'fox')
