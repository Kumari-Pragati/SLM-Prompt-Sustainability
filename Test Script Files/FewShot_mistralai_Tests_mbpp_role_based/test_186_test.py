import unittest
from mbpp_186_code import check_literals

class TestCheckLiterals(unittest.TestCase):
    def test_matches_pattern(self):
        self.assertEqual(check_literals("Hello World", r'\bHello\b'), 'Matched!')
        self.assertEqual(check_literals("123456789", r'\d+'), 'Matched!')
        self.assertEqual(check_literals("Python Programming", r'\w+'), 'Matched!')

    def test_no_match(self):
        self.assertEqual(check_literals("Hello World", r'\d+'), 'Not Matched!')
        self.assertEqual(check_literals("123456789", r'\w+'), 'Not Matched!')
        self.assertEqual(check_literals("Python Programming", r'\d+'), 'Not Matched!')

    def test_empty_string(self):
        self.assertEqual(check_literals("", r'\w+'), 'Not Matched!')

    def test_invalid_pattern(self):
        self.assertRaises(Exception, check_literals, "Hello World", 123)
