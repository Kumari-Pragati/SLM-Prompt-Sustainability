import unittest
from mbpp_186_code import check_literals

class TestCheckLiterals(unittest.TestCase):
    def test_match_found(self):
        self.assertEqual(check_literals('Hello, world!', ['world']), 'Matched!')

    def test_no_match_found(self):
        self.assertEqual(check_literals('Hello, world!', ['foo']), 'Not Matched!')

    def test_multiple_matches(self):
        self.assertEqual(check_literals('Hello, world! world!', ['world']), 'Matched!')

    def test_empty_pattern(self):
        self.assertEqual(check_literals('Hello, world!', []), 'Not Matched!')

    def test_empty_text(self):
        self.assertEqual(check_literals('', ['world']), 'Not Matched!')

    def test_pattern_not_found(self):
        self.assertEqual(check_literals('Hello, world!', ['bar']), 'Not Matched!')

    def test_pattern_found_at_start(self):
        self.assertEqual(check_literals('world, hello!', ['world']), 'Matched!')

    def test_pattern_found_at_end(self):
        self.assertEqual(check_literals('hello, world!', ['world']), 'Matched!')

    def test_pattern_found_multiple_times(self):
        self.assertEqual(check_literals('world, world, hello!', ['world']), 'Matched!')

    def test_pattern_found_at_start_and_end(self):
        self.assertEqual(check_literals('world, hello, world!', ['world']), 'Matched!')
