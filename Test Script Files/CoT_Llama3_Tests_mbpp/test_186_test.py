import unittest
from mbpp_186_code import check_literals

class TestCheckLiterals(unittest.TestCase):
    def test_match(self):
        self.assertEqual(check_literals('hello world', ['hello']), 'Matched!')

    def test_no_match(self):
        self.assertEqual(check_literals('hello world', ['goodbye']), 'Not Matched!')

    def test_multiple_matches(self):
        self.assertEqual(check_literals('hello world hello', ['hello']), 'Matched!')

    def test_no_patterns(self):
        self.assertEqual(check_literals('hello world', []), 'Not Matched!')

    def test_empty_text(self):
        self.assertEqual(check_literals('', ['hello']), 'Not Matched!')

    def test_empty_pattern(self):
        self.assertEqual(check_literals('hello world', ['']), 'Not Matched!')

    def test_invalid_pattern(self):
        with self.assertRaises(re.error):
            check_literals('hello world', ['[hello')
