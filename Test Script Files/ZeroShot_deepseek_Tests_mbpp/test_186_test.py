import unittest
from mbpp_186_code import check_literals

class TestCheckLiterals(unittest.TestCase):

    def test_matched(self):
        self.assertEqual(check_literals('Hello, World!', ['World']), 'Matched!')

    def test_not_matched(self):
        self.assertEqual(check_literals('Hello, World!', ['Python']), 'Not Matched!')

    def test_multiple_patterns(self):
        self.assertEqual(check_literals('Hello, World!', ['World', 'Python']), 'Matched!')

    def test_empty_text(self):
        self.assertEqual(check_literals('', ['World']), 'Not Matched!')

    def test_empty_patterns(self):
        self.assertEqual(check_literals('Hello, World!', []), 'Not Matched!')
