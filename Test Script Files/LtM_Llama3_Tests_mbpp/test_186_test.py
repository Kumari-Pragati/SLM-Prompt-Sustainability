import unittest
from mbpp_186_code import check_literals

class TestCheckLiterals(unittest.TestCase):
    def test_simple_match(self):
        self.assertEqual(check_literals('Hello World', ['Hello']), 'Matched!')

    def test_simple_no_match(self):
        self.assertEqual(check_literals('Hello World', ['Goodbye']), 'Not Matched!')

    def test_empty_text(self):
        self.assertEqual(check_literals('', ['Hello']), 'Not Matched!')

    def test_empty_patterns(self):
        self.assertEqual(check_literals('Hello World', []), 'Not Matched!')

    def test_single_pattern_match(self):
        self.assertEqual(check_literals('Hello World', ['World']), 'Matched!')

    def test_single_pattern_no_match(self):
        self.assertEqual(check_literals('Hello World', ['Moon']), 'Not Matched!')

    def test_multiple_patterns_match(self):
        self.assertEqual(check_literals('Hello World, Goodbye Moon', ['Hello', 'Goodbye']), 'Matched!')

    def test_multiple_patterns_no_match(self):
        self.assertEqual(check_literals('Hello World, Goodbye Moon', ['Sun', 'Rain']), 'Not Matched!')
