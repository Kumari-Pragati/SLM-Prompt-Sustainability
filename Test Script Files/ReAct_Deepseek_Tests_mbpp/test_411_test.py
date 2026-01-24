import unittest
from mbpp_411_code import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):

    def test_single_word_snake_case(self):
        self.assertEqual(snake_to_camel('hello'), 'Hello')

    def test_multiple_words_snake_case(self):
        self.assertEqual(snake_to_camel('hello_world'), 'HelloWorld')

    def test_empty_string(self):
        self.assertEqual(snake_to_camel(''), '')

    def test_all_lowercase_snake_case(self):
        self.assertEqual(snake_to_camel('lowercase_words'), 'LowercaseWords')

    def test_all_uppercase_snake_case(self):
        self.assertEqual(snake_to_camel('UPPERCASE_WORDS'), 'UppercaseWords')

    def test_mixed_case_snake_case(self):
        self.assertEqual(snake_to_camel('MiXeD_CaSe_SnAkE'), 'MixedCaseSnake')

    def test_single_underscore_snake_case(self):
        self.assertEqual(snake_to_camel('_single_underscore'), 'SingleUnderscore')

    def test_trailing_underscore_snake_case(self):
        self.assertEqual(snake_to_camel('trailing_underscore_'), 'TrailingUnderscore')

    def test_leading_underscore_snake_case(self):
        self.assertEqual(snake_to_camel('_leading_underscore'), 'LeadingUnderscore')

    def test_double_underscore_snake_case(self):
        self.assertEqual(snake_to_camel('double__underscore'), 'DoubleUnderscore')
