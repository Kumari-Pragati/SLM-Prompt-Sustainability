import unittest
from mbpp_186_code import check_literals

class TestCheckLiterals(unittest.TestCase):

    def test_empty_text(self):
        self.assertEqual(check_literals('', ['[a-z]+']), 'Not Matched!')

    def test_single_pattern(self):
        self.assertEqual(check_literals('abc', ['[a-z]+']), 'Matched!')
        self.assertEqual(check_literals('123', ['[a-z]+']), 'Not Matched!')

    def test_multiple_patterns(self):
        self.assertEqual(check_literals('abc123', ['[a-z]+', '[0-9]+']), 'Matched!')
        self.assertEqual(check_literals('abc123', ['[a-z]+', '[A-Z]+']), 'Not Matched!')

    def test_complex_pattern(self):
        self.assertEqual(check_literals('The quick brown fox jumps over the lazy dog', ['The [a-z]+ [a-z]+ [a-z]+ [a-z]+ [a-z]+', 'jumps']), 'Matched!')
        self.assertEqual(check_literals('The quick brown fox jumps over the lazy dog', ['The [a-z]+ [a-z]+ [a-z]+ [a-z]+ [a-z]+', 'lazy cat']), 'Not Matched!')
