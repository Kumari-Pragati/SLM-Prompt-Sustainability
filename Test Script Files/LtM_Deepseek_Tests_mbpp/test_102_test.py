import unittest
from mbpp_102_code import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(snake_to_camel('simple_case'), 'SimpleCase')

    def test_single_word(self):
        self.assertEqual(snake_to_camel('word'), 'Word')

    def test_empty_string(self):
        self.assertEqual(snake_to_camel(''), '')

    def test_all_lowercase(self):
        self.assertEqual(snake_to_camel('all_lowercase'), 'AllLowercase')

    def test_with_numbers(self):
        self.assertEqual(snake_to_camel('with_123'), 'With123')

    def test_with_special_characters(self):
        self.assertEqual(snake_to_camel('with_special@#$characters'), 'WithSpecial@#$Characters')

    def test_leading_underscore(self):
        self.assertEqual(snake_to_camel('_leading_underscore'), 'LeadingUnderscore')

    def test_trailing_underscore(self):
        self.assertEqual(snake_to_camel('trailing_underscore_'), 'TrailingUnderscore')

    def test_multiple_underscores(self):
        self.assertEqual(snake_to_camel('multiple__underscores'), 'MultipleUnderscores')
