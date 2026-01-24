import unittest
from mbpp_482_code import match

class TestMatch(unittest.TestCase):
    def test_match_uppercase_and_lowercase(self):
        self.assertEqual(match('HelloWorld'), 'Yes')

    def test_match_all_uppercase(self):
        self.assertEqual(match('HELLO'), 'Yes')

    def test_match_all_lowercase(self):
        self.assertEqual(match('helloworld'), 'No')

    def test_match_no_match(self):
        self.assertEqual(match('hello'), 'No')

    def test_match_empty_string(self):
        self.assertEqual(match(''), 'No')
