import unittest
from mbpp_477_code import is_lower

class TestIsLower(unittest.TestCase):

    def test_lowercase_string(self):
        self.assertEqual(is_lower('abc'), 'abc')

    def test_uppercase_string(self):
        self.assertEqual(is_lower('ABC'), 'abc')

    def test_mixed_case_string(self):
        self.assertEqual(is_lower('AbC'), 'abc')

    def test_empty_string(self):
        self.assertEqual(is_lower(''), '')

    def test_string_with_numbers(self):
        self.assertEqual(is_lower('aB2'), 'ab2')
