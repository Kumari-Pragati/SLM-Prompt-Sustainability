import unittest
from mbpp_186_code import check_literals

class TestCheckLiterals(unittest.TestCase):

    def test_match(self):
        self.assertEqual(check_literals('Hello, world!', ['Hello']), 'Matched!')

    def test_no_match(self):
        self.assertEqual(check_literals('Hello, world!', ['Goodbye']), 'Not Matched!')

    def test_multiple_matches(self):
        self.assertEqual(check_literals('Hello, world! Goodbye, world!', ['Hello', 'Goodbye']), 'Matched!')

    def test_no_matches(self):
        self.assertEqual(check_literals('Hello, world!', []), 'Not Matched!')

    def test_empty_text(self):
        self.assertEqual(check_literals('', ['Hello']), 'Not Matched!')

    def test_empty_pattern(self):
        self.assertEqual(check_literals('Hello, world!', ['']), 'Not Matched!')

    def test_pattern_with_spaces(self):
        self.assertEqual(check_literals('Hello, world!', ['Hello world']), 'Matched!')

    def test_pattern_with_special_characters(self):
        self.assertEqual(check_literals('Hello, world!', ['Hello.*']), 'Matched!')
