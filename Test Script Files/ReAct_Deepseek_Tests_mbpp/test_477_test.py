import unittest
from mbpp_477_code import is_lower

class TestIsLower(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(is_lower('Hello'), 'hello')

    def test_empty_string(self):
        self.assertEqual(is_lower(''), '')

    def test_already_lowercase(self):
        self.assertEqual(is_lower('hello'), 'hello')

    def test_special_characters(self):
        self.assertEqual(is_lower('HeLLo WoRLd!'), 'hello world!')

    def test_numbers_and_symbols(self):
        self.assertEqual(is_lower('123@#$'), '123@#$')

    def test_whitespace(self):
        self.assertEqual(is_lower('Hello World'), 'hello world')

    def test_unicode(self):
        self.assertEqual(is_lower('Héllo Wôrld'), 'héllo wôrld')
